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
    def __init__(self, title, isfinish = False):
        self.title = title
        self.isfinish = isfinish

    def finish(self):
        self.isfinish = True

    def ret_dict(self):
        return {self.title:self.isfinish}



class ToDoList:
    def __init__(self):
        self.__task_list = []
        self.__task_dict = {}

    # list待办任务
    def ls_task(self):
        for n,task in enumerate(self.__task_list):
            print(f"------->序号:{n} --- 任务:{task.title} --- 完成情况isfinish:{task.isfinish}")

    # 添加待办任务
    def add_task(self,title,isfinish = False):
        task = Task(title,isfinish)
        self.__task_list.append(task)

    # 删除待办任务
    def del_task(self,title):
        self.__task_list = [task for task in self.__task_list if task.title != title]

    # 标记完成任务
    def finish_task(self,title):
        for n,task in enumerate(self.__task_list):
            if task.title == title:
                self.__task_list[n].finish()

    # 保存任务到JSON
    def save_task(self,filename):
        try :
            self.__task_dict.clear()
            for task in self.__task_list:
                self.__task_dict[task.title] = task.isfinish
            with open(filename,'w') as f:
                json.dump(self.__task_dict, f, indent=4)
            return True
        except :
            return False

    # 读取JSON到系统
    def read_task(self,filename):
        try :
            self.__task_dict.clear()
            with open(filename,'r') as f:
                self.__task_dict = json.load(f)
            for key,value in self.__task_dict.items():
                self.add_task(key,value)
            return True
        except :
            return False

def main():

    filename = "/home/fire/AI_Agent/Python/day07_project/todo.json"

    todo = ToDoList()
    if todo.read_task(filename):
        print("从系统读取配置成功")
    else:
        print("从系统读取配置失败")
        
    print("<------------------------------------------------------------------------------->")
    print("--->欢迎使用待办任务管理系统")
    print("--->选项 0 --- list待办任务")
    print("--->选项 1 --- 添加待办任务")
    print("--->选项 2 --- 删除待办任务")
    print("--->选项 3 --- 标记完成任务")
    print("<------------------------------------------------------------------------------->")

    try:
        while True:
            index_int = int(input("输入选项(int):"))
            
            match index_int:

                # list待办任务
                case 0:
                    todo.ls_task()
                    
                # 添加待办任务
                case 1:
                    title = input("输入--添加待办任务--名称(str):")
                    todo.add_task(title)
                    
                # 删除待办任务
                case 2:
                    title = input("输入--删除待办任务--名称(str):")
                    todo.del_task(title)

                # 标记完成任务
                case 3:
                    title = input("输入--标记完成任务--名称(str):")
                    todo.finish_task(title)

                case _:
                    pass

    except KeyboardInterrupt:
        # 保存任务到JSON
        if todo.save_task(filename) == False:
            print("\n保存JSON失败")
        else:
            print("\n保存JSON成功")
        



if __name__ == "__main__":
    main()