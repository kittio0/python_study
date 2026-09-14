from pathlib import Path
import json

from py基础代码练习.json解析.aa import user, contents

path=Path('ab.json')
def write(path):
    user={}
    user["name"]=input("请输入你的姓名：")
    user["age"]=int(input("请输入你的年龄："))
    contents=json.dump(user,ensure_ascii=False)
    path.write_text(contents, encoding="utf-8")


def read(path):
    user={}
    contents=path.read_text()
    user=json.loads(contents)

if path.exists():
    read(path)
else:
    write(path)
