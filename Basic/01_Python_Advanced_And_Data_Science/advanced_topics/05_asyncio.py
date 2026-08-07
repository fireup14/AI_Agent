# 05_asyncio.py
# Python 异步编程 (Asyncio) 练习
import asyncio
import time
import random

# 任务：模拟并发 LLM API 请求。
# 1. 编写一个 async 函数 mock_llm_request(prompt_id)。
#    该函数使用 asyncio.sleep 模拟网络等待时间（随机 1 至 3 秒），
#    然后返回 f"Prompt {prompt_id} response: Done"。
# 2. 在 main 函数中，使用 asyncio.gather 并发运行 5 个 mock_llm_request。
# 3. 统计并对比并发执行的总耗时与串行执行的耗时差异。

async def mock_llm_request(prompt_id: int) -> str:
    delay = random.uniform(1.0, 3.0)
    print(f"[Start] Request {prompt_id} sending (simulated delay: {delay:.2f}s)...")
    # 使用 asyncio.sleep 挂起协程，不要使用 time.sleep
    await asyncio.sleep(delay)
    print(f"[Done] Request {prompt_id} finished.")
    return f"Prompt {prompt_id} response: Done"

async def main():
    start_time = time.perf_counter()
    
    # 提示：在这里使用 asyncio.gather 传入 5 个任务
    results = await asyncio.gather(
        mock_llm_request(0),
        mock_llm_request(1),
        mock_llm_request(2),
        mock_llm_request(3),
        mock_llm_request(4),
        )
     
    end_time = time.perf_counter()
    print(f"\n并发执行 5 个请求总共耗时: {end_time - start_time:.2f} 秒")

if __name__ == "__main__":
    print("--- 异步并发测试 ---")
    asyncio.run(main())
 