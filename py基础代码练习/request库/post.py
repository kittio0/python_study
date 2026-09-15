import requests

url = "https://api.deepseek.com/v1/chat/completions"
key = "skv-"
headers = {
    "Authorization": f"Bearer {key}",
    "Content-Type": "application/json"
}
question = input("输入问题：").strip()
body={
    "model": "deepseek-flash",
    "messages": 
    [
        {
            "role": "user",
            "content": question
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