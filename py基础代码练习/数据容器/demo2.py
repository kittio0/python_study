# 数据容器：列表（list）学习笔记

# list=[1,2,2,4]
#
# list.append(5) #添加元素
# print(list)
#
# list.insert(0,0) #插入元素
# print(list)
#
# list.pop(1) #删除指定索引的元素
# print(list)
#
# list.remove(2) #删除与之一样的元素
# print(list)
#
# list.reverse() #反转列表
# print(list)
#
# list.sort() #排序
# print(list)
#
# print(list[0])#最小值
# print(list[-1])#最大值
# print(sum(list)/len(list))#平均值

# 合并列表，并去除重复元素
a=[1,2,3,45,7,68,52]
b=[1,4,3,8,52,11]

c=a+b
d=[]
for i in c:
    if i not in d:
        d.append(i)
print(d)

#随机生成20个数，取出其中的偶数并平方
import random

x=[]
for i in range(20):
    x.append(random.randint(1,10))
y=[]
for i in x:
    if i%2==0:
        y.append(i**2)
print(y)
