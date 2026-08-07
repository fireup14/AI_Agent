# 02_decorators.py
# Python 装饰器 (Decorators) 练习
import time
import functools

# 任务：编写一个计时装饰器 @timer，用于测量任意函数的执行时间。
# 提示：使用 time.perf_counter() 或 time.time() 来计算耗时，
# 使用 @functools.wraps(func) 来保留原函数的元数据（如函数名、文档）。

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # 在这里写下计时逻辑
        # 1. 记录开始时间
        start_time = time.perf_counter()
        # 2. 执行原函数并获取返回值
        result = func(*args, **kwargs)
        # 3. 记录结束时间，计算差值并打印
        end_time = time.perf_counter()
        elapsed = end_time - start_time
        print(f"函数 {func.__name__} 运行时间为： {elapsed:.6f} s")
        # 4. 返回原函数结果
        return result
    return wrapper


@timer
def heavy_calculation(n):
    """模拟一个耗时的计算过程"""
    total = 0
    for i in range(n):
        total += i
    return total

if __name__ == "__main__":
    print("--- 装饰器测试 ---")
    print("计算结果:", heavy_calculation(10))
