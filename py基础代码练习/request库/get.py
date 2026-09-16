import requests

host = "k66r738e2p.re.qweatherapi.com" 
city_url = f"https://{host}/geo/v2/city/lookup"
weather_url = f"https://{host}/v7/weather/now"

headers = {
    "Content-Type": "application/json"
}
def get_city_id():
    """获取城市ID"""
    position=input("请输入城市名称：")
    params={
        "key":"*****",
        "location":position
    }
    try:
        response=requests.get(city_url,params=params,headers=headers)
        response.raise_for_status()
        re=response.json()
        # print(re.keys())
        if re["code"]!="200":
            print("没找到城市")
            return None,0
        else:
            a=re["location"][0]
            return a["id"],1
            # print(f"城市ID：{a['id']}")
            # print(f"城市名称：{a['name']}")
            # print(f"城市经度：{a['lon']}")
            # print(f"城市纬度：{a['lat']}")
            # print(f"城市时区：{a['tz']}")
            # print(f"城市经纬度：{a['adm2']}")
    except requests.exceptions.ConnectTimeout:
        print("连接超时")
    except requests.exceptions.Timeout:
        print("请求超时")
    except requests.exceptions.HTTPError:
        print(f"HTTP错误,状态码:{response.status_code}")
    except KeyError:
        print("返回json缺少字段,格式异常")
    except Exception as e:
        print(f"未知错误：{e}")
    return None,0

def get_weather(city_id):
    """获取天气信息"""
    params={
        "key":"*****",
        "location":city_id
    }
    try:
        response=requests.get(weather_url,params=params,headers=headers)
        response.raise_for_status()
        re=response.json()
        if re["code"]!="200":
            print(f"查询失败,返回码:{re['code']}")
            return None
        # print(re.keys())
        now=re["now"]
        print(f"温度：{now['temp']}℃")
        print(f"体感温度：{now['feelsLike']}℃")
        print(f"天气：{now['text']}")
        print(f"风向：{now['windDir']}")
        return re['now']
    except requests.exceptions.ConnectTimeout:
        print("连接超时")
    except requests.exceptions.Timeout:
        print("请求超时")
    except requests.exceptions.HTTPError:
        print(f"HTTP错误,状态码:{response.status_code}")
    except KeyError:
        print("返回json缺少字段,格式异常")
    except Exception as e:
        print(f"未知错误：{e}")
    return None





if __name__ == "__main__":
    try:
        city_id, flag = get_city_id()
        print(city_id)
        if flag == 1:
            weather = get_weather(city_id)
        else:
            print("没有找到城市")
    except KeyboardInterrupt:
        print("\n程序被用户手动退出")
