# Day 2: Control Flow & Basic Data Structures
# 请在此编写第二天的练习代码

# 任务 1：猜数字游戏
# 预设一个数字（例如 42），让用户循环输入猜测，提示“大了”或“小了”，猜对时退出循环。
def guess_number():
    target = 42
    # 在这里写下你的代码
    while True :
        num_str = input("输入您的猜测结果(int):")
        num = int(num_str)
        if num > target :
            print("猜大了")
        elif num < target :
            print("猜小了")
        else:
            break
    print("恭喜你！！！猜对了")
    pass

# 任务 2：成绩统计
# 让用户依次输入 5 个学生的成绩存入列表，最后输出最高分、最低分以及平均分。
def grade_statistics():
    # 在这里写下你的代码
    list_score = []
    for i in range(5):
        score = int(input(f"请输入第{i+1}个学生的成绩:"))
        list_score.append(score)

    score_max = max(list_score)
    score_min = min(list_score)
    score_len = len(list_score)
    score_sum = sum(list_score)
    score_mean = score_sum / score_len

    print(f"最高分{score_max},最低分{score_min},平均分{score_mean}")
    pass

if __name__ == "__main__":
    print("--- Day 2 Practice ---")
    # 取消下方注释来测试你的函数：
    # guess_number()
    # grade_statistics()
