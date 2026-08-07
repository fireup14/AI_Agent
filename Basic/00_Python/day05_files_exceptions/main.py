# Day 5: File Operations & Exception Handling
# 请在此编写第五天的练习代码
import json
import os

# 任务 1：记账日志程序
# 用户输入消费项目和金额，程序将其追加写入到 expenses.txt 中。
# 再次启动时，程序能读取该文件并计算总支出。
def expense_tracker():

    filename = "/home/fire/AI_Agent/Python/day05_files_exceptions/expenses.txt"
    coin_sum = 0.0

    # 在这里写下你的代码
    try :
        # 1---打开文件读取内容
        with open(filename, 'r', encoding="utf-8") as f:
            content_r = f.read()

        # 2---字符串处理
        for str_cn in ["--消费项目", "----消费金额", "\n"]:
            content_r = content_r.replace(str_cn,"")
        content_list = content_r.split(':')

        # 3---列表筛选金额并打印
        for n in range(len(content_list)):
            try :
                coin_sum += float(content_list[n])
            except ValueError:
                pass
        print(f"--- 历史消费金额总数为: {coin_sum:.2f}")
        
    except FileNotFoundError :
        print("--- 未查到历史消费信息")


    # 4---写文件新的内容
    with open(filename, 'a', encoding="utf-8") as f:
        Prj = input("---> 新增消费项目: ")
        Amount = input("---> 新增消费金额: ")
        content_w = "--消费项目:" + Prj + '\n' "----消费金额:" + Amount + '\n'
        f.write(content_w)


# 任务 2：配置读取器
# 尝试读取一个 JSON 配置文件，如果文件不存在，捕获 FileNotFoundError，并自动创建一个默认的 JSON 配置写入磁盘。
def config_reader():

    config_file = "/home/fire/AI_Agent/Python/day05_files_exceptions/config.json"
    default_config = {
        "username": "default_user",
        "theme": "dark",
        "version": "1.0.0",
        "islonly": True
    }

    try :
        with open(config_file, 'r', encoding="utf-8") as f:
            std_str = json.load(f)
            print(std_str)
    except FileNotFoundError:
        with open(config_file, 'w', encoding="utf-8") as f:
            json.dump(default_config, f, indent = 4)
        


if __name__ == "__main__":
    print("--- Day 5 Practice ---")
    # 取消下方注释来测试你的函数：
    expense_tracker()
    # config_reader()
