

def x(a):
    return a+1,a+2
print(x(1))

def calc(x):
    print("进入calc函数")
    y = x * x
    return y

def a():
    a = 3
    b = calc(a)
    print(b)

a()

#*args只能封装位置参数，不能封装关键字参数
def ab(*args):
    max1=max(args)
    min1=min(args)
    avger1=sum(args)/len(args)
    return max1,min1,avger1

list=ab(1,4,4,58,2,75,74)
print(list)

#**kwargs可以封装关键字参数
def abc(**kwargs):
    print(kwargs)


abc(a=1,b=2,c=3)

add=lambda a,b:a+b
print(add(1,2))

#阶乘函数
def jc(n):
    if n==1:
        return 1
    else:
        return n*jc(n-1)

re=jc(5)
print(re)


# 案例 定义一个用于根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额的函数。
#
# 具体规则如下：
#
# 1. 优惠券需要商品金额满 5000 才可以使用，且优惠券金额不能超过商品总价。
# 2. 积分抵扣需要商品总金额满 5000 才可以使用，100 积分抵扣 1 元（且抵扣金额不能超过商品总价，积分只能整百抵扣）。

def money(coupon,points,freight,**kyargs):
    #全部金额
    total_sum=0;
    for v in kyargs.values():
        total_sum+=v["price"]*v["quantity"]
    if total_sum>=5000:
        if coupon>total_sum:
            coupon=total_sum
        use=points//100*100
        points1=use/100
        if points1>total_sum:
            points1=total_sum
        return total_sum-coupon-points+freight
    else:
      return total_sum


x={"goods1":{"price":1000,"quantity":10},"goods2":{"price":2000,"quantity":5}}
a=money(coupon=1000,points=2000,freight=100,**x)
print(a)



