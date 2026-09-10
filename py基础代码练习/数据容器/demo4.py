
#元组  不可修改
t1 = (80, 95, 78, 50, 76, 80, 85, 20)

print(t1)
print(type(t1))


print(t1[0])
print(t1[-1])

print(t1[0:5:1])

# count() 统计元素的个数
print(t1.count(80))

# index() 获取元素的索引(第一个元素的位置)
print(t1.index(80))

# #组包
# a=(1,2,3,4,56)
# b=1,2,3,4,56
#
# print(a)
# print(b)
#
# #解包
# x,y,z,m,n=a
# print(x,y,z,m,n)
#
# #
# *x, y = a
# print(x,y)

# 交换变量的值
a=1
b=2
c=3

a,b,c=c,a,b

print(a,b,c)


