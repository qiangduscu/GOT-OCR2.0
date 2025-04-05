import os
import json
import tempfile
import zipfile
import subprocess
from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.responses import JSONResponse
from fastapi.responses import StreamingResponse
import asyncio
from multiprocessing import Pool
from GOT.eval.eval_GOT_ocr import eval_model
from GOT.demo.run_ocr_2_0 import eval_model as recognizer_model
from argparse import Namespace
import shutil

app = FastAPI()

def run_eval(chunk_id, model_name, gtfile_path, image_path, out_path, num_chunks, datatype, temperature):
    
    # 设置 GPU 可见性
    os.environ["CUDA_VISIBLE_DEVICES"] = str(chunk_id)
    
    # 构建参数对象
    args = Namespace(
        model_name=model_name,
        gtfile_path=gtfile_path,
        image_path=image_path,
        out_path=out_path,
        num_chunks=num_chunks,
        chunk_idx=chunk_id,
        datatype=datatype,
        temperature=temperature,
        conv_mode=None  # 根据实际情况调整
    )
    
    # 执行评估逻辑
    eval_model(args)

def run_command(cmd, error_msg):
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise HTTPException(status_code=500, detail=f"{error_msg}: {result.stderr}")
    return result

@app.post("/test/")
async def test():
    print("收到请求！")
    return {"status": "ok"}

@app.post("/image_ocr/", response_class=JSONResponse)
async def image_ocr(
    image: UploadFile = File(...),
    ocr_model_name: str = Form("/home/cncs-ai/work/deep_learning/GOT-OCR2.0/output/20250322-fulldata"),
    datatype: str = Form('OCR', description="数据类型: Text/Doc/VQAv2/Cap"),                    
):
    print("收到请求！")
    # 将图片保存到本地
    with tempfile.TemporaryDirectory() as tmp_dir:
        image_file = os.path.join(tmp_dir, image.filename)
        with open(image_file, "wb") as f:
            shutil.copyfileobj(image.file, f)
        # 调用OCR模型进行识别

        # --- 执行评估流程 ---
        out_dir = os.path.join(tmp_dir, "output")
        os.makedirs(out_dir, exist_ok=True)
        # 构建参数对象
        args = Namespace(
            model_name=ocr_model_name,
            image_file=image_file,
            type=datatype,
            box='',
            color='',
            render=False,
        )
        result = recognizer_model(args)
        print("识别结果：", result)
        return result

@app.post("/evaluate/", response_class=JSONResponse)
async def evaluate(
    # image_zip: UploadFile = File(..., description="包含批量图片的ZIP压缩包"),
    # gt_file: UploadFile = File(..., description="包含图片路径的JSON汇总文件"),
    gt_data: str = Form(..., description="直接传递的JSON数据（不再是文件）"), 
    ocr_model_name: str = Form("/home/cncs-ai/work/deep_learning/GOT-OCR2.0/output/20250322-fulldata"),
    num_chunks: int = Form(2),
    temperature: float = Form(0.2),
    datatype: str = Form('OCR', description="数据类型: Text/Doc/VQAv2/Cap"),
):
    print("收到批量请求！")
    # 提前读取文件内容到内存，确保在生成器执行前完成
    # image_data = await image_zip.read()
    # gt_data = await gt_file.read()    
    # gt_data = await json.loads(gt_file)
    async def generate_progress():
        try:
            # 步骤1: 初始化
            yield "开始处理请求...\n"
            
            # 步骤2: 处理图片压缩包
            # yield "正在解压图片\n"
            with tempfile.TemporaryDirectory() as tmp_dir:
                image_dir = os.path.join(tmp_dir, "images")
                # os.makedirs(image_dir)
                # zip_path = os.path.join(tmp_dir, "images.zip")
                # await asyncio.to_thread(lambda: open(zip_path, "wb").write(image_data))
                # await asyncio.to_thread(lambda: zipfile.ZipFile(zip_path).extractall(image_dir))
                # yield "图片解压完成\n"
                yield "正在执行识别任务...请稍后...\n"

                # 步骤3: 处理GT文件
                gt_path = os.path.join(tmp_dir, "gt.json")
                # await asyncio.to_thread(lambda: open(gt_path, "wb").write(gt_data))
                await asyncio.to_thread(lambda: open(gt_path, "wb").write(gt_data.encode("utf-8")))

                # --- 执行评估流程 ---
                out_dir = os.path.join(tmp_dir, "output")
                os.makedirs(out_dir, exist_ok=True)

                # 步骤4: 执行评估命令（异步）
                with Pool(num_chunks) as p:
                    for i in range(num_chunks):
                        chunk_id = i
                        p.apply_async(run_eval, (chunk_id, ocr_model_name, gt_path,
                                                image_dir, out_dir, num_chunks, datatype, temperature))
                    p.close()
                    p.join()

                # 合并结果
                yield "正在合并结果 \n"
                merge_cmd = [
                    "python3", "-m", "GOT.eval.pyevaltools.merge_results",
                    "--out_path", out_dir,
                ]
                run_command(merge_cmd, "结果合并失败")

                # 查找并返回结果文件
                yield "查找并返回结果文件 \n"
                result_file = next((f for f in os.listdir(out_dir) if f.endswith(".json")), None)
                if not result_file:
                    yield "[ERROR] 未找到结果文件\n"
                    raise HTTPException(status_code=500, detail="未找到结果文件")
                
                # 读取结果文件
                result_path = os.path.join(out_dir, result_file)
                with await asyncio.to_thread(open, result_path) as f:
                    result_data = await asyncio.to_thread(json.load, f)
                
                # 最终结果标记
                yield f"[RESULT] {json.dumps(result_data, ensure_ascii=False)}\n"

        except zipfile.BadZipFile:
            yield "[ERROR] 无效的ZIP文件格式\n"
            raise HTTPException(status_code=400, detail="无效的ZIP文件格式")
        except HTTPException as he:
            yield f"[ERROR] HTTP异常: {he.detail}\n"
            raise
        except Exception as e:
            yield f"[ERROR] 未处理的异常: {str(e)}\n"
            raise HTTPException(status_code=500, detail=f"服务器内部错误: {str(e)}")
    
    return StreamingResponse(generate_progress(), media_type="text/plain")
        
