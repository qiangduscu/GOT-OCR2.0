@app.post("/evaluate/", response_class=JSONResponse)
async def evaluate(
    gt_data: str = Form(..., description="直接传递的JSON数据（不再是文件）"), 
    ocr_model_name: str = Form("/home/cncs-ai/work/deep_learning/GOT-OCR2.0/output/20250322-fulldata"),
    num_chunks: int = Form(2),
    temperature: float = Form(0.2),
    datatype: str = Form('OCR', description="数据类型: Text/Doc/VQAv2/Cap"),
):
    async def generate_progress():
        try:
            # 步骤1: 初始化
            yield "开始处理请求...\n"
            
            with tempfile.TemporaryDirectory() as tmp_dir:
                image_dir = os.path.join(tmp_dir, "images")
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