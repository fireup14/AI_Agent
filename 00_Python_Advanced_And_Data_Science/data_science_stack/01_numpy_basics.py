"""NumPy 与向量化思维练习。

本文件提供观察实验、独立练习和验收断言，不包含 TODO 的实现答案。
建议依次完成：数组基础 → 矩阵乘法 → 广播与 Z-Score。
"""

import time

import numpy as np
import numpy.typing as npt


FloatArray = npt.NDArray[np.float64]


def demonstrate_matrix_multiplication(
    size: int = 80,
    seed: int = 42,
) -> None:
    """观察 Python 三层循环与 NumPy 向量化矩阵乘法的耗时差异。

    这是已完成的观察实验，无需修改。
    """

    rng = np.random.default_rng(seed)
    matrix_a = rng.random((size, size))
    matrix_b = rng.random((size, size))

    start = time.perf_counter()
    loop_result = np.zeros((size, size))
    for row in range(size):
        for column in range(size):
            for index in range(size):
                loop_result[row, column] += (
                    matrix_a[row, index] * matrix_b[index, column]
                )
    loop_time = time.perf_counter() - start

    start = time.perf_counter()
    numpy_result = matrix_a @ matrix_b
    numpy_time = time.perf_counter() - start

    assert np.allclose(loop_result, numpy_result)
    print(f"Python 三层循环：{loop_time:.4f} 秒")
    print(f"NumPy 矩阵乘法：{numpy_time:.4f} 秒")
    print(f"本次实验加速比：{loop_time / numpy_time:.2f} 倍")


def reshape_and_filter(values: npt.ArrayLike) -> tuple[FloatArray, FloatArray]:
    """题目 1：数组创建、形状、变形和布尔索引。

    要求：
    1. 把 values 转换为 float64 的 NumPy 数组；
    2. 确保数组恰好包含 12 个元素，否则抛出 ValueError；
    3. 将数组变形为 3×4；
    4. 使用布尔索引选出所有大于数组均值的元素；
    5. 返回 ``(reshaped, filtered)``，不得使用 Python 循环。

    预期：
        matrix, selected = reshape_and_filter(range(12))
        matrix.shape == (3, 4)
        selected == [6, 7, 8, 9, 10, 11]
    """
    array = np.asarray(values,dtype=np.float64)
    # print(array)

    if array.size != 12:
        raise ValueError("数组并非恰好包含 12 个元素")
    
    reshape_arr = array.reshape(3,-1)
    # print(reshape_arr)

    filter_arr = array[array>array.mean()]
    # print(filter_arr)

    return (reshape_arr,filter_arr)

def manual_matrix_multiply(
    matrix_a: FloatArray,
    matrix_b: FloatArray,
) -> FloatArray:
    """题目 2：手写小型二维矩阵乘法。

    要求：
    1. 检查两个参数都是二维数组；
    2. 检查 matrix_a 的列数等于 matrix_b 的行数；
    3. 维度不合法时抛出 ValueError；
    4. 使用 Python 三层循环计算，不得在函数内部使用 ``@`` 或 np.dot；
    5. 返回新的 float64 数组。

    完成后使用 ``matrix_a @ matrix_b`` 验证结果。
    """
    if (matrix_a.ndim != 2) or (matrix_b.ndim != 2):
        raise ValueError("两个矩阵维度不匹配")

    ( end_line , colu) = matrix_a.shape
    ( line , end_clou) = matrix_b.shape

    if colu != line:
        raise ValueError("矩阵无法进行乘法运算")

    result = np.zeros((end_line,end_clou),dtype=np.float64)
    for i in range(end_line):
        for j in range(end_clou):
            for num in range(line):
                result[i,j] += (
                    matrix_a[i,num] * matrix_b[num,j]
                )
    return result




def zscore_normalize(data: FloatArray) -> FloatArray:
    """题目 3：使用广播完成按列 Z-Score 标准化。

    要求：
    1. data 必须是二维数组，否则抛出 ValueError；
    2. 使用 axis=0 计算每列均值和标准差；
    3. 某列标准差为 0 时抛出 ValueError；
    4. 使用广播计算 ``(data - mean) / std``；
    5. 不得使用逐行或逐列 Python 循环。

    验收：
        标准化后每列均值应接近 0，标准差应接近 1。
    """
    if data.ndim != 2:
        raise ValueError("data不是二维数组")

    mean = data.mean(axis = 0)
    std = data.std(axis = 0)

    if np.any(np.isclose(std,0.0)):
        raise ValueError("某列标准差为 0")

    z_score= (data - mean) / std
    return z_score



def run_checks() -> None:
    """完成全部题目后运行的基础验收。"""

    matrix, selected = reshape_and_filter(range(12))
    assert matrix.shape == (3, 4)
    assert matrix.dtype == np.float64
    assert np.array_equal(selected, np.arange(6, 12, dtype=np.float64))

    matrix_a = np.array([[1.0, 2.0], [3.0, 4.0]])
    matrix_b = np.array([[5.0, 6.0], [7.0, 8.0]])
    assert np.allclose(
        manual_matrix_multiply(matrix_a, matrix_b),
        matrix_a @ matrix_b,
    )

    rng = np.random.default_rng(42)
    data = rng.normal(size=(100, 5))
    normalized = zscore_normalize(data)
    assert normalized.shape == (100, 5)
    assert np.allclose(normalized.mean(axis=0), 0.0, atol=1e-10)
    assert np.allclose(normalized.std(axis=0), 1.0, atol=1e-10)

    print("NumPy 基础验收通过。")


if __name__ == "__main__":
    demonstrate_matrix_multiplication()

    # 完成全部题目后取消下一行注释：
    run_checks()
