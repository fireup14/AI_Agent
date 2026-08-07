# Day 7: Final Project - CLI To-Do App
# 命令行待办事项管理器
# 
# 目标：
# 1. 允许用户添加、标记完成、查看、删除待办任务。
# 2. 采用面向对象设计（如 Task 类和 TodoList 类）。
# 3. 程序退出时自动将数据保存到 json 文件中，启动时自动加载。
# 4. 健壮的异常捕获与友好的交互界面。

import json
import os

class Task:
    def __init__(self, title, is_completed=False):
        self.title = title
        self.is_completed = is_completed

    def to_dict(self):
        return {"title": self.title, "is_completed": self.is_completed}

    @classmethod
    def from_dict(cls, data):
        return cls(data["title"], data["is_completed"])


class TodoList:
    def __init__(self, filename="todo_data.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def add_task(self, title):
        # 添加任务
        pass

    def complete_task(self, index):
        # 标记第 index 个任务为已完成
        pass

    def delete_task(self, index):
        # 删除第 index 个任务
        pass

    def view_tasks(self):
        # 打印任务列表
        pass

    def save_tasks(self):
        # 保存任务到 JSON 文件
        pass

    def load_tasks(self):
        # 从 JSON 文件加载任务
        pass


def main():
    todo = TodoList()
    print("=== 欢迎使用 Python 命令行待办事项管理器 ===")
    
    while True:
        print("\n可选操作:")
        print("1. 查看任务列表")
        print("2. 添加新任务")
        print("3. 标记任务完成")
        print("4. 删除任务")
        print("5. 保存并退出")
        
        choice = input("请输入操作编号 (1-5): ").strip()
        
        if choice == "1":
            todo.view_tasks()
        elif choice == "2":
            title = input("请输入任务内容: ").strip()
            if title:
                todo.add_task(title)
        elif choice == "3":
            todo.view_tasks()
            try:
                idx = int(input("请输入要标记完成的任务序号: ")) - 1
                todo.complete_task(idx)
            except ValueError:
                print("请输入有效的数字！")
        elif choice == "4":
            todo.view_tasks()
            try:
                idx = int(input("请输入要删除的任务序号: ")) - 1
                todo.delete_task(idx)
            except ValueError:
                print("请输入有效的数字！")
        elif choice == "5":
            todo.save_tasks()
            print("数据已保存，再见！")
            break
        else:
            print("无效输入，请重新输入！")

if __name__ == "__main__":
    main()
