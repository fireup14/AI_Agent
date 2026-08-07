# Day 1: Python Basics & Environment
# 请在此编写第一天的练习代码

# 任务 1：温度转换器
# 接收用户输入的摄氏温度，计算并输出华氏温度（公式：F = C * 1.8 + 32）。
def temp_converter():
    # 在这里写下你的代码
    C_str = input("请输入摄氏温度(小数点后保留至少一位):")
    C_float = float(C_str)
    F = C_float * 1.8 + 32
    print(f"华氏温度:{F:.2f}")
    pass

# 任务 2：个人信息生成器
# 通过 input 收集用户的姓名、年龄、身高，然后用 f-string 格式化输出一段完整的自我介绍。
def profile_generator():
    # 在这里写下你的代码
    name_str = input("输入姓名(str):")
    age_str = input("输入年龄(int):")
    height_str = input("输入身高(float):")
    
    age_int = int(age_str)
    height_float = float(height_str)

    print(f"姓名 {name_str} , 年龄 {age_int} , 身高 {height_float} 。")
    pass

if __name__ == "__main__":
    print("--- Day 1 Basics Practice ---")
    # 取消下方注释来测试你的函数：
    temp_converter()
    # profile_generator()
