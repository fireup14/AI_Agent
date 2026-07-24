# Day 4: Functions & Modules
# 请在此编写第四天的练习代码

# 导入自定义模块
import calculator

# 任务 2：斐波那契数列生成器
# 编写一个函数，接收参数 N，返回含有前 N 个斐波那契数的列表。
def fibonacci(n=5):
    # 在这里写下你的代码
    a,b = 0,1
    list_fib = []

    for i in range(n):
        a,b = b,a+b
        list_fib.append(a)

    return list_fib
    pass

if __name__ == "__main__":
    print("--- Day 4 Practice ---")
    
    # 测试自定义计算器模块
    # print("10 + 5 =", calculator.add(10, 5))
    # print("10 / 0 =", calculator.divide(10, 0))
    
    # 测试斐波那契函数
    print("Fibonacci(10):", fibonacci(10))
