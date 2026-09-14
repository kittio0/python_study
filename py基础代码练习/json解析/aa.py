
from pathlib import Path
import json

path=Path('ab.json')

user={}
user["name"]=input("请输入你的姓名：")
user["age"]=int(input("请输入你的年龄："))

contents=json.dumps(user,ensure_ascii=False)
path.write_text(contents,encoding="utf-8")