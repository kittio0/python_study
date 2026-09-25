# py基础代码练习

## 内容

### 1. 基础语法与流程控制（demo1.py）
- 变量定义、多变量赋值、`type()` 与 `isinstance()` 类型判断
- `print` 输出、转义字符与引号、`input()` 输入
- 算术运算：`/` 除法与 `//` 整除的区别
- 分支语句 `if / elif / else`（三角形类型判断）
- `match...case` 模式匹配与守卫条件（简易计算器）
- `for` + `range()` 累加求和
- 嵌套 `for` 循环（打印九九乘法表）
- `while True` + `break` 配合 `random.randint()`（猜数字游戏）

### 2. 数据容器
- 列表 `append` / `insert` / `pop` / `remove` 增删改查
- 列表 `reverse` / `sort` 排序、索引取值、`sum()`/`len()` 求平均
- 列表切片与列表推导式
- 列表综合练习：合并去重保持顺序、筛选偶数并求平方
- 字符串下标访问与正负步长切片
- 字符串常用方法：`find` / `count` / `upper` / `lower` / `replace`
- 元组的索引、切片与不可变性
- 元组组包解包、星号解包 `*x, y = a`、交换变量
- 集合的创建、`add` / `remove`、`set()` 对列表去重
- 集合运算：`&` 交集、`-` 差集（选修课名单统计）
- 字典的创建、按键取值改值、`items()` 遍历
- 嵌套字典存数据（购物车管理系统）

### 3. 函数
- 函数定义、调用与多返回值（元组形式）
- 函数之间的相互调用
- 可变参数 `*args` 与 `**kwargs`
- `lambda` 匿名函数
- 递归函数（`jc()` 计算阶乘）
- 综合案例：订单金额计算（满 5000 才可用优惠券与积分，100 积分抵 1 元）

### 4. 类与对象
- 类的定义、`__init__` 构造方法与属性
- `__str__` 定制对象的打印格式
- 用默认参数按需修改属性（`update()` 只改指定科目）
- `if __name__ == "__main__"` 写自测代码
- 用列表保存对象、面向对象封装（教务管理系统）
- 输入校验与异常处理：非整数抛 `ValueError` 后重新输入、限制 0~100 分
- 菜单驱动 `while True` + `match...case`，捕获 `KeyboardInterrupt` / `EOFError` 优雅退出

### 5. JSON 与文件读写
- `json.dumps` / `json.loads` 序列化与反序列化
- `ensure_ascii=False` 让中文不被转义成 `\uXXXX`
- `Path.read_text()` / `Path.write_text()` 文件读写
- `path.exists()` 分支判断，把读写逻辑合并成一个程序

### 6. 网络请求与大模型调用（request库/）
- `requests` 发 GET 请求：`params`、`headers`、`raise_for_status()`
- 解析接口返回的嵌套 JSON，取出城市 id 与实时天气字段
- 逐个捕获网络异常：`ConnectTimeout` / `Timeout` / `HTTPError` / `KeyError`
- `requests` 发 POST 请求、`json=` 传参、`Authorization: Bearer <key>` 认证
- 大模型对话的消息结构：`system` 约定角色与规则 + `user` 传数据
- 综合实战：把天气接口数据交给 DeepSeek 生成口语化天气播报

## 验收

1. `demo1.py` 正常运行，猜数字游戏猜中后正常结束
2. 五个数据容器的 demo 输出与注释描述一致
3. 列表、集合、字典的综合练习结果正确
4. 函数综合案例算出的订单金额符合注释里的优惠规则
5. 学生类能正确打印各科成绩与总分，`update()` 只改指定科目
6. 教务管理系统增删改查正常，姓名重复不会重复添加
7. 教务管理系统输入非法成绩时会提示并让人重新输入
8. 教务管理系统的菜单和 `Ctrl+C` 都能正常退出程序
9. JSON 读写往返正常，文件不存在时能自动创建
10. `combine.py` 在文件存在与不存在两种情况下都能正常工作
11. `get.py` 能查到指定城市天气，城市不存在时有明确提示
12. `post.py` 能基于天气数据生成播报，且不会把原始 JSON 直接输出
13. 接口超时或网络异常时程序不崩溃，有明确错误提示

> 环境要求：Python 3.10+（用到 `match...case`）；除 `request库/` 外只用标准库，`request库/` 需 `pip install requests`；`json解析/` 和 `request库/` 有相对路径依赖，需先 `cd` 进各自目录再运行。
