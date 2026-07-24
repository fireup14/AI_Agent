# calculator.py
# 简易计算器模块 - Day 4 任务 1

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # 提示：处理除以零的情况
    if b == 0:
        return "Error: Division by zero!"
    return a / b
