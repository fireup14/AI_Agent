# tool_calling.py
# 阶段 5：大模型工具调用 (Tool Calling) 基础

import os
from openai import OpenAI
import json

# 配置 API 密钥与地址
api_key = os.getenv("OPENAI_API_KEY", "your-api-key-here")
base_url = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
client = OpenAI(api_key=api_key, base_url=base_url)

# 1. 定义本地工具函数
def get_current_weather(city: str) -> str:
    """获取指定城市的当前天气情况"""
    # 实际开发中，这里会调用第三方天气 API。此处返回模拟数据。
    city_lower = city.lower()
    if "北京" in city_lower or "beijing" in city_lower:
        return json.dumps({"city": "北京", "temperature": "26°C", "condition": "晴天"})
    elif "上海" in city_lower or "shanghai" in city_lower:
        return json.dumps({"city": "上海", "temperature": "22°C", "condition": "阴天"})
    else:
        return json.dumps({"city": city, "temperature": "未知", "condition": "未知"})


# 2. 定义提供给大模型的工具声明列表 (Tools Schema)
tools_schema = [
    {
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "获取指定城市的当前天气情况",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "城市名称，例如：北京、上海",
                    }
                },
                "required": ["city"],
            },
        },
    }
]

def run_tool_calling_loop():
    print("--- 智能体工具调用测试 ---")
    user_prompt = "请帮我查一下上海的天气怎么样？"
    print(f"用户问题: {user_prompt}")
    
    messages = [{"role": "user", "content": user_prompt}]
    
    # 1. 询问大模型，并附带工具定义
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        tools=tools_schema,
        tool_choice="auto" # 让大模型自主选择是否调用工具
    )
    
    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls
    
    # 2. 检查大模型是否作出了工具调用决策
    if tool_calls:
        print("\n大模型决定调用外部工具！")
        messages.append(response_message) # 把大模型的回复保存进对话历史
        
        # 3. 模拟执行本地对应的工具函数
        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_args = json.loads(tool_call.function.arguments)
            
            print(f"调用的函数名: {function_name}")
            print(f"解析出的参数: {function_args}")
            
            if function_name == "get_current_weather":
                # 执行真实函数
                tool_output = get_current_weather(city=function_args.get("city"))
                print(f"本地工具返回的数据: {tool_output}")
                
                # 4. 把工具的执行结果传回大模型，角色标记为 "tool"
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "name": function_name,
                    "content": tool_output,
                })
        
        # 5. 再次请求大模型，让大模型整合工具数据并回答用户
        second_response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )
        print("\n大模型最终的回答：")
        print(second_response.choices[0].message.content)
    else:
        print("\n大模型没有调用工具，直接回复：")
        print(response_message.content)


if __name__ == "__main__":
    # run_tool_calling_loop()
    pass
