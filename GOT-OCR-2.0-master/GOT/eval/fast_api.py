import os
import json
import tempfile
import zipfile
import subprocess
from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.responses import JSONResponse
from fastapi.responses import StreamingResponse
import asyncio

app = FastAPI()

def run_command(cmd, error_msg):
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise HTTPException(status_code=500, detail=f"{error_msg}: {result.stderr}")
    return result

@app.post("/test/")
async def test():
    print("收到请求！")
    return {"status": "ok"}

@app.post("/evaluate/", response_class=JSONResponse)
async def evaluate(
    image_zip: UploadFile = File(..., description="包含批量图片的ZIP压缩包"),
    gt_file: UploadFile = File(..., description="包含图片路径的JSON汇总文件"),
    ocr_model_name: str = Form("/home/cncs-ai/work/deep_learning/GOT-OCR2.0/output/20250322-fulldata"),
    num_chunks: int = Form(1),
    temperature: float = Form(0.2),
    datatype: str = Form('OCR', description="数据类型: Text/Doc/VQAv2/Cap"),
):
    # 提前读取文件内容到内存，确保在生成器执行前完成
    image_data = await image_zip.read()
    gt_data = await gt_file.read()    
    async def generate_progress():
        try:
            # 步骤1: 初始化
            yield "开始处理请求...\n"
            
            # 步骤2: 处理图片压缩包
            yield "解压图片文件中...\n"
            with tempfile.TemporaryDirectory() as tmp_dir:
                image_dir = os.path.join(tmp_dir, "images")
                os.makedirs(image_dir)
                zip_path = os.path.join(tmp_dir, "images.zip")
                await asyncio.to_thread(lambda: open(zip_path, "wb").write(image_data))
                await asyncio.to_thread(lambda: zipfile.ZipFile(zip_path).extractall(image_dir))
                yield "图片解压完成\n"

                # 步骤3: 处理GT文件
                yield "处理GT文件中...\n"
                gt_path = os.path.join(tmp_dir, "gt.json")
                await asyncio.to_thread(lambda: open(gt_path, "wb").write(gt_data))
                yield "GT文件处理完成\n"

                # --- 执行评估流程 ---
                out_dir = os.path.join(tmp_dir, "output")
                os.makedirs(out_dir, exist_ok=True)

                # 步骤4: 执行评估命令（异步）
                yield "执行评估流程...请稍后...\n"
                eval_cmd = [
                    "python3", "-m", "GOT.eval.multi_hardware_eval_GOT",
                    "--model-name", ocr_model_name,
                    "--gtfile_path", gt_path,
                    "--image_path", image_dir,
                    "--out_path", out_dir,
                    "--num-chunks", str(num_chunks),
                    "--temperature", str(temperature),
                    "--datatype", datatype,
                ]
                proc = await asyncio.create_subprocess_exec(
                    *eval_cmd,
                    stdout=asyncio.subprocess.PIPE,
                    stderr=asyncio.subprocess.PIPE
                )
                while True:
                    output = await proc.stdout.readline()
                    if not output:
                        break
                    yield f"[评估日志] {output.decode().strip()}\n"

                # 合并结果
                yield "正在合并结果"
                merge_cmd = [
                    "python3", "-m", "GOT.eval.pyevaltools.merge_results",
                    "--out_path", out_dir,
                ]
                run_command(merge_cmd, "结果合并失败")

                # OCR评估（固定使用plain类型）
                yield "OCR评估（固定使用plain类型）"
                ocr_cmd = [
                    "python3", "-m", "GOT.eval.pyevaltools.eval_ocr",
                    "--out_path", out_dir,
                    "--gt_path", gt_path,
                    "--datatype", datatype,
                ]
                run_command(ocr_cmd, "OCR评估失败")

                # 查找并返回结果文件
                yield "查找并返回结果文件"
                result_file = next((f for f in os.listdir(out_dir) if f.endswith(".json")), None)
                if not result_file:
                    yield "[ERROR] 未找到结果文件\n"
                    raise HTTPException(status_code=500, detail="未找到结果文件")
                
                # 读取结果文件
                result_path = os.path.join(out_dir, result_file)
                with await asyncio.to_thread(open, result_path) as f:
                    result_data = await asyncio.to_thread(json.load, f)
                
                # 最终结果标记
                yield f"[RESULT] {json.dumps(result_data)}\n"

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
        
