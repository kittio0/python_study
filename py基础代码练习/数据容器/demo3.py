# 数据容器：字符串（str）学习笔记


s="abcdefg-abab"

print(s)
print(s[2])
print(s[0:5:1])
print(s[-1:-6:-1])

#find 查找子字符串，返回第一次出现的索引，没有返回-1
index=s.find("c")
print(index)

#count 统计子串在字符串中出现的次数
count=s.count("a")
print(count)

#upper 转大写
s=s.upper()
print(s)

#lower 转小写
s=s.lower()
print(s)

#replace 替换子串
s=s.replace("a","x")
print(s)

