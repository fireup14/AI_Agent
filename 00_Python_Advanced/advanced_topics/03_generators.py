"""Python 生成器练习。

学习顺序：
1. 阅读每道题的要求与示例；
2. 独立补全标有 TODO 的函数；
3. 每完成一题，单独运行对应示例；
4. 全部完成后，取消文件末尾 ``run_checks()`` 的注释进行验证。

注意：本文件只提供题目、提示和验收代码，不包含实现答案。
"""

from collections.abc import Iterable, Iterator
from pathlib import Path
import sys
import time
from typing import TypeVar


T = TypeVar("T")


# ---------------------------------------------------------------------------
# 观察实验（无需修改）
# ---------------------------------------------------------------------------
def memory_comparison(limit: int = 1_000_000) -> None:
    """观察列表与生成器对象在创建时间和对象大小上的差异。

    sys.getsizeof() 只统计对象本身的大小，不递归统计所有元素，
    因此结果适合用于理解趋势，不应当视为完整的进程内存报告。
    """

    print("--- 列表与生成器对比 ---")

    start_time = time.perf_counter()
    large_list = [number for number in range(limit)]
    list_time = time.perf_counter() - start_time
    list_memory = sys.getsizeof(large_list) / (1024 * 1024)
    print(f"列表创建时间：{list_time:.4f} 秒，对象大小：{list_memory:.2f} MB")

    start_time = time.perf_counter()
    large_generator = (number for number in range(limit))
    generator_time = time.perf_counter() - start_time
    generator_memory = sys.getsizeof(large_generator)
    print(
        f"生成器创建时间：{generator_time:.4f} 秒，"
        f"对象大小：{generator_memory} Bytes"
    )


# ---------------------------------------------------------------------------
# 题目 1：基础 yield
# ---------------------------------------------------------------------------
def countdown(start: int) -> Iterator[int]:
    """从 start 倒数到 1，每次产生一个整数。

    要求：
    1. 使用 yield，不得创建并返回完整列表；
    2. start 等于 0 时不产生任何值；
    3. start 小于 0 时抛出 ValueError；
    4. 不要修改函数签名。

    预期：
        list(countdown(3)) == [3, 2, 1]
        list(countdown(0)) == []

    提示：
        yield 会暂停函数，并保存当前局部变量和执行位置。
    """

    # TODO: 请独立完成
    raise NotImplementedError


# ---------------------------------------------------------------------------
# 题目 2：惰性读取文件
# ---------------------------------------------------------------------------
def read_large_file(file_path: str | Path) -> Iterator[str]:
    """逐行读取 UTF-8 文本文件，每次产生一行内容。

    要求：
    1. 使用 with 打开文件；
    2. 直接遍历文件对象，不使用 read() 或 readlines()；
    3. 去掉每行末尾的换行符后再 yield；
    4. 不要捕获 FileNotFoundError，让调用者决定如何处理。

    提示：
        文件对象本身就是可迭代对象。
        可以使用 line.rstrip("\\n")，注意不要删除行首空格。
    """

    # TODO: 请独立完成
    raise NotImplementedError


# ---------------------------------------------------------------------------
# 题目 3：组合生成器管道
# ---------------------------------------------------------------------------
def filter_lines(
    lines: Iterable[str],
    keyword: str,
) -> Iterator[str]:
    """从任意字符串可迭代对象中，惰性产生包含 keyword 的行。

    要求：
    1. 匹配时忽略大小写；
    2. 保持原始行内容不变；
    3. 不要把 lines 转换为 list；
    4. keyword 为空字符串时抛出 ValueError。

    预期：
        source = ["INFO ready", "ERROR failed", "error timeout"]
        list(filter_lines(source, "error"))
        == ["ERROR failed", "error timeout"]

    思考：
        为什么参数写成 Iterable[str]，返回值写成 Iterator[str]？
    """

    # TODO: 请独立完成
    raise NotImplementedError


# ---------------------------------------------------------------------------
# 题目 4：yield from
# ---------------------------------------------------------------------------
def flatten(groups: Iterable[Iterable[T]]) -> Iterator[T]:
    """将多组可迭代数据惰性展开为一层。

    要求：
    1. 使用 yield from；
    2. 不得创建保存全部结果的新列表；
    3. 保留元素原有类型。

    预期：
        list(flatten([[1, 2], [3], [], [4, 5]]))
        == [1, 2, 3, 4, 5]

        list(flatten([("a", "b"), ("c",)]))
        == ["a", "b", "c"]
    """

    # TODO: 请独立完成
    raise NotImplementedError


# ---------------------------------------------------------------------------
# 题目 5：保存生成器状态
# ---------------------------------------------------------------------------
def fibonacci(count: int) -> Iterator[int]:
    """依次产生指定数量的斐波那契数：0、1、1、2、3……

    要求：
    1. 使用局部变量保存相邻的两个数；
    2. 每轮只计算下一个值，不预先生成列表；
    3. count 等于 0 时不产生值；
    4. count 小于 0 时抛出 ValueError。

    预期：
        list(fibonacci(0)) == []
        list(fibonacci(1)) == [0]
        list(fibonacci(7)) == [0, 1, 1, 2, 3, 5, 8]
    """

    # TODO: 请独立完成
    raise NotImplementedError


# ---------------------------------------------------------------------------
# 综合题：文件读取 + 过滤管道
# ---------------------------------------------------------------------------
def find_errors(file_path: str | Path) -> Iterator[str]:
    """组合已有生成器，惰性产生日志中包含 ERROR 的行。

    要求：
    1. 复用 read_large_file() 和 filter_lines()；
    2. 不要重复实现文件读取或过滤规则；
    3. 尝试使用 yield from。
    """

    # TODO: 请独立完成
    raise NotImplementedError


def run_checks() -> None:
    """全部题目完成后运行的基础验收。"""

    assert list(countdown(3)) == [3, 2, 1]
    assert list(countdown(0)) == []

    source = ["INFO ready", "ERROR failed", "error timeout"]
    assert list(filter_lines(source, "error")) == [
        "ERROR failed",
        "error timeout",
    ]

    assert list(flatten([[1, 2], [3], [], [4, 5]])) == [1, 2, 3, 4, 5]
    assert list(flatten([("a", "b"), ("c",)])) == ["a", "b", "c"]

    assert list(fibonacci(0)) == []
    assert list(fibonacci(1)) == [0]
    assert list(fibonacci(7)) == [0, 1, 1, 2, 3, 5, 8]

    for invalid_call in (lambda: countdown(-1), lambda: fibonacci(-1)):
        try:
            next(invalid_call())
        except ValueError:
            pass
        else:
            raise AssertionError("负数参数应当抛出 ValueError")

    print("基础验收通过。请继续手动验证文件读取和综合题。")


if __name__ == "__main__":
    memory_comparison()

    # 完成所有题目后，取消下一行注释：
    # run_checks()
