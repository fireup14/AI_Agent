# 01_dunder_methods.py
# Python 魔法方法 (Dunder Methods) 练习

# 任务：设计一个 Vector2D（二维向量）类，实现以下功能：
# 1. 构造函数 __init__ 接收 x 和 y。
# 2. 魔法方法 __str__ 和 __repr__ 返回向量的字符串表示（如 "Vector2D(3, 4)"）。
# 3. 魔法方法 __add__ 实现两个向量相加（v1 + v2），返回一个新的 Vector2D 对象。
# 4. 魔法方法 __mul__ 实现向量数乘（v * scalar），返回一个新的 Vector2D 对象。
# 5. 魔法方法 __len__ 返回向量长度的整数部分（或者向量的维度，这里返回 2 即可）。

import math

class Vector2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    # 在这里实现魔法方法
    def __str__(self):
        return f"({self.x},{self.y})"
    
    def __repr__(self):
        return f"向量 = ({self.x},{self.y})"

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
        
    def __mul__(self, num):
        return Vector2D(self.x * num, self.y * num)
    
    def __len__(self):
        # 修正：__len__ 必须返回整数，这里进行取整
        return int((self.x ** 2 + self.y ** 2) ** 0.5)

    def __rmul__(self, num):
        # 支持数乘交换律：num * v
        return self.__mul__(num)

if __name__ == "__main__":
    print("--- 魔法方法测试 ---")
    v1 = Vector2D(3, 4)
    v2 = Vector2D(1, 2)
    print(v1) 
    print(v1 + v2) 
    print(v1 * 3)
    print(3 * v1)  # 测试 __rmul__
    print(len(v1)) # 测试 __len__ (模长应为 5)


