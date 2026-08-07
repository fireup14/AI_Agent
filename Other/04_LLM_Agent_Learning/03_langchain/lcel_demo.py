# lcel_demo.py
# 阶段 3：使用 LangChain Expression Language (LCEL) 构建极简翻译链

import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 配置 API 密钥与地址
api_key = os.getenv("OPENAI_API_KEY", "your-api-key-here")
base_url = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")

def run_translation_chain():
    print("--- LangChain LCEL 翻译链测试 ---")
    
    # 1. 初始化模型
    model = ChatOpenAI(
        model="gpt-4o-mini",
        openai_api_key=api_key,
        openai_api_base=base_url
    )
    
    # 2. 创建提示词模板
    prompt = ChatPromptTemplate.from_messages([
        ("system", "你是一个翻译官。请把用户的句子翻译成{target_language}，只返回翻译结果，不要做任何解释。"),
        ("user", "{text}")
    ])
    
    # 3. 创建输出解析器
    output_parser = StrOutputParser()
    
    # 4. 使用 LCEL ( | 运算符) 拼接链路
    chain = prompt | model | output_parser
    
    # 5. 调用链路
    try:
        result = chain.invoke({
            "target_language": "法语",
            "text": "人生苦短，我用 Python。"
        })
        print("翻译结果：", result)
    except Exception as e:
        print("运行出错：", e)


if __name__ == "__main__":
    # run_translation_chain()
    pass
