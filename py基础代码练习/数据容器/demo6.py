

#字典dict
d1 = {"name": "张三", "age": 18, "sex": "男"}
print(d1)
print(type(d1))
print(d1["name"])
d1["name"]="123"
print(d1["name"])

a=d1.items()
print(a)

for key,v in d1.items():
    print(f"{key}:{v}",end="\t")

# 开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用字典结构存储商品数据，通过控制台菜单与用户交互。具体功能如下：
#
# 1．添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
#
# 2．修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
#
# 3．删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
#
# 4．查询购物车：将购物车中的商品信息展示出来，格式为："商品名称：xxx，商品价格：xxx，商品数量：xxx"。
#
# 5．退出购物车

#制作·菜单
menu = """
*************************
*      1.添加购物车       *        
*      2.修改购物车       *        
*      3.删除购物车       *        
*      4.查询购物车       *        
*      5.退出购物车       *    
*************************
"""
while True:
    print(menu)
    choice = input("请输入你的选择：")

    buy={"a":{"price":1,"quantity":1},"b":{"price":2,"quantity":2}}
    #执行具体操作
    match choice:
        case "1": # 添加购物车
            name=input("请输入商品名称：")
            price=input("请输入商品价格：")
            quantity=input("请输入商品数量：")
            if name in buy:
                print("商品已存在")
            else:
                buy[name]={"price":price,"quantity":quantity}
                print("添加成功")

        case "2": # 修改购物车
            name=input("请输入要修改的购物车商品名称：")
            price=input("请输入商品价格：")
            quantity=input("请输入商品数量：")
            if name in buy:
                buy[name]={"price":price,"quantity":quantity}
                print("修改成功")
            else:
                print("商品不存在,请重新操作")

        case "3": # 删除购物车
            name=input("请输入要删除的购物车商品名称：")
            if name in buy:
                del buy[name]
                print("删除成功")
            else:
                print("商品不存在,请重新操作")
        case "4": # 查询购物车
            for k,v in buy.items():
               print(f"商品名称：{k}，商品价格：{v['price']}，商品数量：{v['quantity']}")

        case "5": # 退出购物车
            print("退出购物车")
            break
        case _:
            print("输入错误")










