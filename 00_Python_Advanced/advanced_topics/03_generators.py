# 03_generators.py
# Python 生成器 (Generators) 练习
import sys
import time

# 任务 1：对比列表与生成器的内存占用和生成速度
# 我们将比较生成 10,000,000 个数字时，列表和生成器的开销。
def task_1_memory_comparison():
    print("--- 任务 1: 内存与性能对比 ---")
    limit = 10000000

    # 1. 列表推导式 (List Comprehension)
    start_time = time.perf_counter()
    large_list = [x for x in range(limit)]
    list_time = time.perf_counter() - start_time
    list_memory = sys.getsizeof(large_list) / (1024 * 1024) # 转换为 MB
    print(f"列表生成时间: {list_time:.4f} 秒, 内存占用: {list_memory:.2f} MB")

    # 2. 生成器表达式 (Generator Expression)
    start_time = time.perf_counter()
    large_gen = (x for x in range(limit))
    gen_time = time.perf_counter() - start_time
    gen_memory = sys.getsizeof(large_gen) / 1024 # 转换为 KB
    print(f"生成器生成时间: {gen_time:.4f} 秒, 内存占用: {gen_memory:.2f} KB")
    
    # 释放内存
    del large_list, large_gen


# 任务 2：大文件生成器读取
# 模拟按行读取一个大型日志文件。如果直接使用 f.readlines() 会将所有内容一次性读入内存，容易内存溢出。
# 请使用 yield 编写一个按行生成内容的生成器函数 read_large_file(file_path)。
def read_large_file(file_path):
    # 在这里编写你的生成器代码
    # 提示：使用 with open(file_path, 'r') as f:
    # 循环遍历 f 并 yield 每一行
    pass


if __name__ == "__main__":
    task_1_memory_comparison()
    
    # 任务 2 测试（可在本地生成一个临时 txt 测试文件）：
    # temp_file = "temp_log.txt"
    # with open(temp_file, "w") as f:
    #     for i in range(100):
    #         f.write(f"Log entry line {i}\n")
    #
    # for line in read_large_file(temp_file):
    #     print(line.strip())
