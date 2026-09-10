# py基础代码学习：基础语法、流程控制、循环

# print(1);
# print("1");
a,num="abab",1;
print("123",a,num)
print(type(a))
# isinstance(a,b) 判断a是否为b类型，返回布尔值
print(isinstance(a,str))
b="abab是‘123’"
print(b)
#不管输入什么，都是字符串
# a=input("请输入：");
# print(a)
# print(type(a))
#/为除以 ，//为整除
print(1/2)
print(1//2)

if a==b:
    print("a不等于b")
    print("123")
print("456")
#判断三角形是否能存在案例
# a=int(input("请输入三角形1的边长："))
# b=int(input("请输入三角形2的边长："))
# c=int(input("请输入三角形3的边长："))
# if a+b>c and a+c>b and b+c>a:
#     print("三角形存在")
#     if a==b and b==c:
#         print("等边三角形")
#     elif a==b or b==c or a==c:
#         print("等腰三角形")
#     else:
#         print("普通三角形")
# else:
#     print("三角形不存在")



# match.....case
# a=input("请输入第一个数：")
# b=input("请输入第二个数：")
# c=input("请输入计算符：")
# match c:
#     case "+":
#         print(f"{a}+{b}={a+b}")
#     case "-":
#         print(f"{a}-{b}={a-b}")
#     case "*":
#         print(f"{a}*{b}={a*b}")
#     case "/"  if b!=0:
#         print(f"{a}/{b}={a/b}")
#     case _:
#         print("输入不符合要求")



x=0;
for i in range(1,101):
    x+=i
print(x)

for i in range(1,11):
    for j in range(1,i+1):
        print(f"{j} * {i} = {i*j}",end="\t")
    print()


import random
num=random.randint(1,100)
print(num)
while True:
    a=int(input("请输入你的猜测："))
    if a>num:
        print("太大了")
    elif a<num:
        print("太小了")
    else:
        print("恭喜你，猜对了")
        break


