# basic_call.py
# 阶段 2：大模型 API 基础调用与 Stream 流式输出

import os
from openai import OpenAI

# 提示：在此处设置你的 API Key 和 Base URL。
# 也可以配置环境变量：export OPENAI_API_KEY="your_api_key"
api_key = os.getenv("OPENAI_API_KEY", "your-api-key-here")
base_url = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1") # 或使用 DeepSeek 等国内大模型节点

# 初始化客户端
client = OpenAI(api_key=api_key, base_url=base_url)

def test_chat_completion():
    print("--- 基础聊天 API 调用 ---")
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini", # 根据你的 Key 修改对应的模型，如 deepseek-chat
            messages=[
                {"role": "system", "content": "你是一个严谨的 AI 助手。"},
                {"role": "user", "content": "请用三句话解释什么是 AI Agent。"}
            ]
        )
        print("回复内容：")
        print(response.choices[0].message.content)
    except Exception as e:
        print("调用出错：", e)


def test_chat_completion_stream():
    print("\n--- 流式输出 (Stream) 聊天调用 ---")
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": "写一首关于 Python 编程的简短现代诗。"}
            ],
            stream=True # 开启流式传输
        )
        
        print("流式回复：", end="", flush=True)
        # 遍历流式返回的 chunk
        for chunk in response:
            content = chunk.choices[0].delta.content
            if content is not None:
                print(content, end="", flush=True)
        print()
    except Exception as e:
        print("调用出错：", e)


if __name__ == "__main__":
    # 执行测试（请先配置好有效的 API 密钥和网络连接）
    # test_chat_completion()
    # test_chat_completion_stream()
    pass
