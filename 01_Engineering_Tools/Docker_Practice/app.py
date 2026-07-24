# app.py
# 一个用于在 Docker 容器内运行的简单 Python 脚本
import time
import os

def main():
    print("--- 欢迎来到 Docker 容器内部！ ---")
    print(f"当前容器内的运行路径: {os.getcwd()}")
    print("准备开始循环输出日志，每 2 秒一次，输出 5 次后退出...")
    
    for i in range(1, 6):
        print(f"[Container Log] Step {i}/5 - Running smoothly...")
        time.sleep(2)
        
    print("运行完成，容器即将退出。")

if __name__ == "__main__":
    main()
