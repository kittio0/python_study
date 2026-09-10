
# set集合
s1 = {1, 2, 3, 4, 5}

print(s1)

#增加元素
s1.add(6)
print(s1)

#删除
s1.remove(2)
print(s1)

#去重最
lst = [1, 1, 2, 2, 3]
s = set(lst)
print(s)


# ------------------------------ 集合 set 案例 ------------------------------
# 选修足球学生名单
football_set = {"王林", "曾牛", "徐立国", "遁天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}
# 选修篮球学生名单
basketball_set = {"张铁", "墨居仁","王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}
# 选修法语学生名单
french_set = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子", "红蝶", "厉飞雨", "韩立", "曾牛"}
# 选修艺术学生名单
art_set = { "遁天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}

# 1. 找出同时选修了 法语 和 艺术 的学生

a = french_set & art_set
print(a)

# 2. 找出同时选修了所有四门课程的学生
b=football_set & basketball_set & french_set & art_set
print(b)

# 3. 找出选修了足球，但是没有选修篮球的学生
c=football_set - basketball_set
print(c)

# 4. 统计每一个学生选修的课程数量
c=[*football_set, *basketball_set, *french_set, *art_set]
for i in c:
    print(f"学生为{i}，选修课程数量为{c.count(i)}")


