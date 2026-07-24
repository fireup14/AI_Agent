# chromadb_demo.py
# 阶段 4：简易向量数据库检索与 RAG 链路

import os
import chromadb
from chromadb.utils import embedding_functions

def run_rag_demo():
    print("--- ChromaDB 向量数据库与轻量级 RAG 演示 ---")
    
    # 1. 初始化 Chroma 本地客户端（数据保存在本地 ./chroma_db 文件夹下）
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    
    # 2. 选择 Embedding 函数 (此处使用默认的 sentence-transformers，本地会自动下载一个微型模型进行计算，无需 API Key)
    # 提示：实际开发中通常使用 OpenAIEmbeddingFunction 等云端 Embedding API
    default_ef = embedding_functions.DefaultEmbeddingFunction()
    
    # 3. 创建或获取一个 Collection (相当于数据库的表)
    collection = chroma_client.get_or_create_collection(
        name="my_notes",
        embedding_function=default_ef
    )
    
    # 4. 模拟准备写入的本地文档
    documents = [
        "小明周六下午 3 点要去羽毛球馆和老张打羽毛球，需要提前带球拍。",
        "Python 进阶语法包括装饰器、生成器、魔法方法和异步协程。",
        "明天的会议在 4 楼 402 会议室召开，时间是早上 9:30，主要讨论 Agent 方案。",
        "Chroma 是一个非常轻量级的开源向量数据库，适合本地快速原型设计。"
    ]
    ids = ["doc1", "doc2", "doc3", "doc4"]
    
    # 写入向量数据库
    print("正在将文档写入本地向量数据库...")
    collection.add(
        documents=documents,
        ids=ids
    )
    print("写入完成。")
    
    # 5. 执行向量检索
    query = "小明这周末有什么安排？"
    print(f"\n用户提问: '{query}'")
    
    results = collection.query(
        query_texts=[query],
        n_results=1 # 只召回最相关的一条文档
    )
    
    retrieved_doc = results['documents'][0][0]
    print(f"检索到的最相关参考资料: {retrieved_doc}")
    
    # 6. RAG 闭环提示构造（模拟发送给 LLM）
    rag_prompt = f"""
    请基于以下参考资料回答问题。如果参考资料里没有提到，请说不知道。
    
    【参考资料】
    {retrieved_doc}
    
    【问题】
    {query}
    """
    
    print("\n--- 最终生成的 RAG 提示词模板 ---")
    print(rag_prompt)

if __name__ == "__main__":
    run_rag_demo()
