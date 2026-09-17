import requests

url = "https://api.deepseek.com/v1/chat/completions"
key = "******"


host = "k66r738e2p.re.qweatherapi.com" 
city_url = f"https://{host}/geo/v2/city/lookup"
weather_url = f"https://{host}/v7/weather/now"

def get_city_id():
    city=input("请输入城市名称：")
    headers = {
        "Content-Type": "application/json"
        }
    params = {
        "location": city,
        "key": "******"
        }

    try:
        re = requests.get(city_url, headers=headers, params=params,timeout=5)
        if re.status_code == 400:
            print("未找到城市")
            return None, 0
        if re.status_code != 200:
            print(f"HTTP错误,状态码:{re.status_code}")
            return None, 0
        r=re.json()
        #print(r.keys())
        if r.get("code") != "200":
            print("未找到城市")
            return None, 0
        c = r["location"][0]
        return c["id"], 1

    except requests.exceptions.ConnectTimeout:
        print("连接超时")
    except requests.exceptions.Timeout:
        print("请求超时")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP错误,状态码:{e.response.status_code}")
    except requests.exceptions.RequestException as e:
        print("请求错误：", e)
    except Exception as e:
        print("未知错误：", e)

    return None, 0
        
def get_weather(id):
    headers = {
        "Content-Type": "application/json"
        }
    params = {
        "location": id,
        "key": "26ebe1c8a9aa4fd5a9a359d6e3c29349"
        }

    try:
        re = requests.get(weather_url, headers=headers, params=params,timeout=5)
        re.raise_for_status()
        r=re.json()
        if r["code"] != "200":  
            print("未找到城市")
            return None
        else:
            c = r["now"]
            return c
    except requests.exceptions.ConnectTimeout:
        print("连接超时")
    except requests.exceptions.Timeout:
        print("请求超时")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP错误,状态码:{e.response.status_code}")
    except requests.exceptions.RequestException as e:
        print("请求错误：", e)
    except Exception as e:
        print("未知错误：", e)

    
    return None

def suggest_weather(weather):
    headers = {
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json"
        }
    body={
        "model": "deepseek-flash",
        "messages": [
            {
                "role": "system",
              "content":  """
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
                "content": 
              f"""
                天气：{weather["text"]}
                温度：{weather["temp"]}
                体感温度：{weather["feelsLike"]}
                风向：{weather["windDir"]}
                风速：{weather["windSpeed"]}
                湿度：{weather["humidity"]}
                
               """
                
            },
        ] 

    }
    try:
        re=requests.post(url, headers=headers, json=body,timeout=20)
        re.raise_for_status()
        r=re.json()
        print(r["choices"][0]["message"]["content"])
    except requests.exceptions.ConnectTimeout:
        print("连接超时")
    except requests.exceptions.ReadTimeout:
        print("读取超时：模型响应太慢，请加大 timeout")
    except requests.exceptions.Timeout:
        print("请求超时")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP错误,状态码:{e.response.status_code}", e.response.text[:200])
    except requests.exceptions.ConnectionError as e:
        print("连接/读取错误：", e)
    except requests.exceptions.RequestException as e:
        print("请求错误：", e)
    except Exception as e:
        print("未知错误：", e)


if __name__ == "__main__":
    id,error=get_city_id()
    try:
        if error==1:
            weather=get_weather(id)
            if weather is None:
                print("天气查询失败，已退出")
            else:
                suggest_weather(weather)
        else:
            print("未找到城市")
    except KeyboardInterrupt:
        print("用户按下Ctrl+C，退出查询")