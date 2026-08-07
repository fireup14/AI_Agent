# structured_output.py
# 阶段 2：使用 Pydantic 实现大模型结构化数据提取 (Structured Outputs)

import os
from openai import OpenAI
from pydantic import BaseModel, Field
from typing import List

# 配置 API 密钥与地址
api_key = os.getenv("OPENAI_API_KEY", "your-api-key-here")
base_url = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
client = OpenAI(api_key=api_key, base_url=base_url)

# 1. 用 Pydantic 定义你期望的数据结构
class MovieInfo(BaseModel):
    title: str = Field(description="电影的中文名称")
    director: str = Field(description="导演的名字")
    release_year: int = Field(description="电影上映年份")
    actors: List[str] = Field(description="前三位主要演员的名字列表")
    rating: float = Field(description="电影的评分（如果是 10 分制）")
    summary: str = Field(description="电影的一句话剧情简介")


def extract_movie_info(review_text: str):
    print("--- 开始提取结构化信息 ---")
    try:
        # 使用 Beta 版本的 chat.completions.parse 接口可以直接自动解析 Pydantic 模型
        # 注意：这需要较新版本的 openai 库和支持 response_format 的模型（如 gpt-4o-mini）
        completion = client.beta.chat.completions.parse(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "你是一个专业的数据抽取助手。请从用户的影评中精确提取出电影信息。"},
                {"role": "user", "content": review_text}
            ],
            response_format=MovieInfo, # 传入 Pydantic 类作为响应格式
        )
        
        # 获取自动解析后的 Pydantic 对象
        movie: MovieInfo = completion.choices[0].message.parsed
        
        print("\n解析成功！提取结果如下：")
        print(f"电影名: {movie.title}")
        print(f"导演: {movie.director}")
        print(f"上映年份: {movie.release_year}")
        print(f"主要演员: {', '.join(movie.actors)}")
        print(f"评分: {movie.rating}")
        print(f"简介: {movie.summary}")
        
        # 验证这是否是真正的 Python 对象
        print(f"类型检查: {type(movie)}")
        
    except Exception as e:
        print("解析失败：", e)


if __name__ == "__main__":
    sample_review = """
    《盗梦空间》（Inception）是一部由克里斯托弗·诺兰执导的经典科幻片。
    该片于 2010 年上映，主演包括莱昂纳多·迪卡普里奥、约瑟夫·高登-莱维特和艾利奥特·佩吉等。
    故事讲述了造梦师团队潜入目标梦境植入想法的冒险过程。豆瓣评分高达 9.4 分，非常值得一看！
    """
    
    # 运行抽取测试
    # extract_movie_info(sample_review)
    pass
