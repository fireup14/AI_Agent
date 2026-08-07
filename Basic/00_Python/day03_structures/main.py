# Day 3: Advanced Data Structures & Strings
# 请在此编写第三天的练习代码

# 任务 1：单词频率统计
# 给定一段英文文本，将其分割成单词，并统计每个单词出现的次数，用字典保存并打印。
def word_count():
    # 在这里写下你的代码
    # 提示：可以使用 text.lower().split()，并用 dict 存储计数

    text = input("输入一段长英文文本：")
    for char in ".?,!;-——":
        text = text.replace(char,' ')
    text_list = text.lower().split()

    dict_en_cnt = {}
    
    for str_en in text_list:
        if str_en in dict_en_cnt:
            dict_en_cnt[str_en] = dict_en_cnt[str_en] + 1
        else:
            dict_en_cnt[str_en] = 1
    
    return dict_en_cnt
    
    pass

# 任务 2：双列表去重复并求交集
# 创建两个含有重复元素的列表，利用集合去除重复，并求出两个列表的共同元素（交集）。
def list_intersection():
    list_a = [1, 2, 3, 4, 4, 5, 6]
    list_b = [4, 5, 5, 6, 7, 8, 9]
    # 在这里写下你的代码
    Aset = set(list_a)
    Bset = set(list_b)
    
    Cset = Aset & Bset
    print(Cset)
    pass

if __name__ == "__main__":
    print("--- Day 3 Practice ---")
    
    # print(word_count())
    list_intersection()
