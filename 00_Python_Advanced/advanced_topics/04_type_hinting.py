# 04_type_hinting.py
# Python 类型提示 (Type Hinting) 练习
#
# 任务：为以下未添加类型提示的函数和类添加完整的类型标注。
# 目标是使代码能够通过 mypy 的静态检查。
# 提示：从 typing 模块中导入 List, Dict, Tuple, Optional, Union, Callable

from typing import List, Dict, Tuple, Optional, Union, Callable

# 1. 基础变量与函数标注
# 任务：为 add 函数及其参数和返回值添加类型提示。
def add(a, b):
    return a + b


# 2. 容器与复杂结构标注
# 任务：为 process_user_data 函数添加类型提示。
# - user_info 应该是一个字典，键为字符串，值为任意类型 (可以使用 Union 或 Any)。
# - 函数返回一个元组，包含一个字符串（用户名）和整型（年龄）。
def process_user_data(user_info):
    username = user_info.get("name", "Unknown")
    age = user_info.get("age", 0)
    return username, age


# 3. 可空类型与默认参数
# 任务：为 find_item 函数添加类型提示。
# - items 应该是一个字符串列表。
# - target 应该是一个字符串。
# - 返回值可以是整型索引，也可以是 None (提示: 使用 Optional 或 Union)。
def find_item(items, target):
    try:
        return items.index(target)
    except ValueError:
        return None


# 4. 类与对象标注
# 任务：为 Task 类的方法添加类型提示（包括构造函数 __init__ 的返回值标注 -> None）。
class Task:
    def __init__(self, title, priority=1):
        self.title = title
        self.priority = priority
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def get_details(self):
        status = "Completed" if self.completed else "Pending"
        return f"[{status}] {self.title} (Priority: {self.priority})"


if __name__ == "__main__":
    print("--- 类型提示练习 ---")
    print("Add (10, 5):", add(10, 5))
    
    user = {"name": "Bob", "age": 25}
    name, age = process_user_data(user)
    print(f"User: {name}, Age: {age}")
    
    my_tasks = ["Study Python", "Read Paper", "Gym"]
    idx = find_item(my_tasks, "Read Paper")
    print("Found 'Read Paper' at index:", idx)
    
    t = Task("Learn PyTorch", priority=3)
    t.mark_completed()
    print(t.get_details())
