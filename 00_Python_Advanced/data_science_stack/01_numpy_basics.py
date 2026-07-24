# 01_numpy_basics.py
# NumPy 科学计算练习
import numpy as np
import time

# 任务 1：对比普通循环与 NumPy 向量化矩阵乘法的速度
# 任务 2：实现 Z-Score 归一化 (X - mean) / std

def task_1_matrix_multiplication():
    # 模拟两个 100x100 的随机矩阵
    size = 100
    A = np.random.rand(size, size)
    B = np.random.rand(size, size)
    
    # 1. 传统 Python 嵌套循环实现
    start = time.perf_counter()
    result_loop = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            for k in range(size):
                result_loop[i, j] += A[i, k] * B[k, j]
    loop_time = time.perf_counter() - start
    print(f"Python 嵌套循环耗时: {loop_time:.4f} 秒")
    
    # 2. NumPy 向量化运算实现 (使用 @ 运算符)
    start = time.perf_counter()
    result_np = A @ B  # 或者 np.dot(A, B)
    np_time = time.perf_counter() - start
    print(f"NumPy @ 运算耗时: {np_time:.4f} 秒")
    print(f"NumPy 速度是循环的 {loop_time / np_time:.2f} 倍！")


def task_2_normalization():
    # 随机生成一个 10x3 的矩阵（模拟 10 个样本，每个样本 3 个特征）
    X = np.random.uniform(10, 100, (10, 3))
    print("\n原始矩阵 X:\n", X)
    
    # 在这里写下归一化代码
    # 提示：计算每列的均值 np.mean(..., axis=0) 和标准差 np.std(..., axis=0)
    # 利用 NumPy 广播机制计算 (X - mean) / std
    pass


if __name__ == "__main__":
    print("--- NumPy 科学计算练习 ---")
    task_1_matrix_multiplication()
    # task_2_normalization()
