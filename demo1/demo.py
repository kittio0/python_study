
# # 功能要求：
# 1. 用venv创建虚拟环境
# 2. 用pip安装requests
# 3. 调用天气API（和风/高德/OpenWeatherMap任选）
# 4. 输入城市名，返回当前温度
# 5. 解析JSON，提取温度、天气、湿度
# 6. 异常处理（城市不存在、网络超时）
# 7. 导出requirements.txt

import requests

url = "https://api.deepseek.com/v1/chat/completions"
key = "******"

host = "k66r738e2p.re.qweatherapi.com"
city_url = f"https://{host}/geo/v2/city/lookup"
weather_url = f"https://{host}/v7/weather/now"


def get_city_id():
    """把用户输入的城市名，换成接口认识的城市 ID。

    Returns:
        tuple: (城市 ID, 状态标志)。成功为 (str, 1)，失败为 (None, 0)
    """

    city=input("请输入城市名称：")
    headers = {
        "Content-Type": "application/json"
        }
    params = {
        "location": city,
        "key": "******"  # 和风天气的密钥
        }

    try:
        re = requests.get(city_url, headers=headers, params=params,timeout=5)
        # 400 表示参数不合法（城市名无法识别），与网络或服务端故障区分开
        if re.status_code == 400:
            print("未找到城市")
            return None, 0
        if re.status_code != 200:
            print(f"HTTP错误,状态码:{re.status_code}")
            return None, 0
        r=re.json()
        # HTTP 200 不代表业务成功，接口自身的返回码才是准的
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
    """根据城市 ID 查当前天气。

    Args:
        id (str): 城市 ID，由 get_city_id() 返回

    Returns:
        dict | None: 查到了返回天气字典（里面有温度、天气状况这些），没查到返回 None
    """

    headers = {
        "Content-Type": "application/json"
        }
    params = {
        "location": id,
        "key": "*****"
        }

    try:
        re = requests.get(weather_url, headers=headers, params=params,timeout=5)

        # 非 2xx 直接抛异常，省去逐项判断状态码
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
    """把天气数据交给大模型，让它写一段人能看懂的口语化播报。

    Args:
        weather (dict): 实时天气数据，由 get_weather() 返回
    """

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
        # 大模型生成比普通接口慢，超时需放宽
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
        # 4xx 的原因写在响应体里（密钥错误、模型名错误等），截断后打印便于定位
        print(f"HTTP错误,状态码:{e.response.status_code}")
    except requests.exceptions.ConnectionError as e:
        print("连接/读取错误：", e)
    except requests.exceptions.RequestException as e:
        print("请求错误：", e)
    except Exception as e:
        print("未知错误：", e)


if __name__ == "__main__":

    # 该调用在 try 之外，此时的 Ctrl+C 不会被下方捕获
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
