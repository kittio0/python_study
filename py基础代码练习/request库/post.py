import requests

from get import get_city_id, get_weather

url = "https://api.deepseek.com/v1/chat/completions"
key = "sk-*******"

headers = {
    "Authorization": f"Bearer {key}",
    "Content-Type": "application/json"
}
city_id = get_city_id()
question = get_weather(city_id)
body={
    "model": "deepseek-flash",
    "messages": 
    [
        {
            "role": "system",
            "content": 
            """
                        你是专业天气播报助手。
                你将接收天气字典question，字段说明：
                temp：温度
                feelsLike：体感温度
                text：天气状况
                windDir：风向
                windSpeed：风速
                humidity：湿度

                任务规则：
                1. 完整展示温度、体感、天气状况、风向、风速、湿度全部天气信息。
                2. 结合天气给出实用生活分析：适合做什么、不建议做什么。
                3. 语言简洁口语化，不要输出原始JSON，不要多余闲聊。
                4. 全部基于传入的数据，严禁编造不存在的天气信息。
            """
        },
        {
            "role": "user",
            "content": f"""
                温度：{question["temp"]}
                体感温度：{question["feelsLike"]}
                天气：{question["text"]}
                风向：{question["windDir"]}
                风速：{question["windSpeed"]}
                湿度：{question["humidity"]}
                """     
        }
    ]
}
try:
    re=requests.post(url,json=body,headers=headers,timeout=20)
    re.raise_for_status()
    r=re.json()
    #print(r["choices"][0]["message"].keys()) 
    content=r["choices"][0]["message"]["content"]
    print(content)
except requests.exceptions.ConnectTimeout:
    print("连接超时")
except requests.exceptions.Timeout:
    print("请求超时")
except requests.exceptions.ConnectionError:
    print("互联网连接错误")
except requests.exceptions.HTTPError:
    print(f"HTTP错误,状态码:{re.status_code}")
except Exception as e:
    print(e)