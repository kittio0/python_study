import requests

host = "k66r738e2p.re.qweatherapi.com" 
url = f"https://{host}/geo/v2/city/lookup"

headers = {
    "Content-Type": "application/json"
}
position=input("请输入城市名称：").split()
params={
    "key":"",
    "location":position
}
try:
    response=requests.get(url,params=params,headers=headers)
    response.raise_for_status()
    re=response.json()
    # print(re.keys())
    a=re["location"][0]
    print(f"城市ID：{a['id']}")
    print(f"城市名称：{a['name']}")
    print(f"城市经度：{a['lon']}")
    print(f"城市纬度：{a['lat']}")
    print(f"城市时区：{a['tz']}")
    print(f"城市经纬度：{a['adm2']}")

except requests.exceptions.ConnectTimeout:
    print("连接超时")
except requests.exceptions.Timeout:
    print("请求超时")
except requests.exceptions.HTTPError:
    print(f"HTTP错误,状态码:{response.status_code}")
except requests.exceptions.KeysError:
    print("返回json缺少字段,格式异常")
except Exception as e:
    print(f"未知错误：{e}")