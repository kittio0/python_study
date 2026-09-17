# py基础代码练习

本目录是 Python 基础语法的练习代码集合，按知识点分成若干子目录，每个文件对应一个主题，文件名 `demoN.py` 表示学习顺序。练习全部围绕标准库展开，只有 `request库/` 用到了第三方库 `requests`。

> 仓库整体说明见上级目录的 [README.md](../README.md)，本文档只介绍本目录内部的文件。

## 目录结构

```
py基础代码练习/
├── demo1.py                 # 基础语法、流程控制、循环
├── requirements.txt         # 依赖清单（仅 request库/ 需要）
├── 数据容器/
│   ├── demo2.py             # 列表 list
│   ├── demo3.py             # 字符串 str
│   ├── demo4.py             # 元组 tuple
│   ├── demo5.py             # 集合 set
│   └── demo6.py             # 字典 dict（购物车管理系统）
├── 函数/
│   └── function1.py         # 函数定义、参数、lambda、递归
├── 类练习/
│   ├── class_student.py     # 类与对象：学生类
│   └── class1.py            # 面向对象综合案例（教务管理系统）
├── json解析/
│   ├── aa.py                # 写入 JSON 文件
│   ├── bb.py                # 读取 JSON 文件
│   ├── combine.py           # 读写合并（文件存在则读，否则写）
│   └── ab.json              # 读写示例用数据文件
└── request库/
    ├── get.py               # GET 请求（和风天气 API）
    └── post.py              # POST 请求（调用 DeepSeek 生成天气播报）
```

## 知识点索引

| 文件 | 主题 | 涉及语法 |
| --- | --- | --- |
| `demo1.py` | 基础语法与流程控制 | 变量、`input`/`print`、`if/elif/else`、`match...case`、`for`、`while`、`random` |
| `数据容器/demo2.py` | 列表 list | 增删改查、`sort`/`reverse`、切片、列表推导 |
| `数据容器/demo3.py` | 字符串 str | 下标、正负步长切片、`find`/`count`/`upper`/`lower`/`replace` |
| `数据容器/demo4.py` | 元组 tuple | 索引、切片、`count`/`index`、组包解包、星号解包 |
| `数据容器/demo5.py` | 集合 set | 去重、交集 `&`、差集 `-`、`count` 统计 |
| `数据容器/demo6.py` | 字典 dict | 嵌套字典、`items()` 遍历、`match...case` 菜单 |
| `函数/function1.py` | 函数 | 多返回值、`*args`/`**kwargs`、`lambda`、递归 |
| `类练习/class_student.py` | 类与对象 | `__init__`、`__str__`、默认参数 |
| `类练习/class1.py` | 面向对象综合 | 类封装、列表存对象、异常处理、菜单驱动 |
| `json解析/aa.py` | 写 JSON | `json.dumps`、`Path.write_text` |
| `json解析/bb.py` | 读 JSON | `json.loads`、`Path.read_text` |
| `json解析/combine.py` | 读写组合 | `Path.exists()` 分支、函数封装 |
| `request库/get.py` | GET 请求 | `requests.get`、`params`、`raise_for_status`、异常分类捕获 |
| `request库/post.py` | POST 请求 | `requests.post`、`json=` 传参、大模型对话消息结构 |

## 各文件说明

### demo1.py — 基础语法与流程控制

- 变量定义与多变量赋值、`print` 输出、`type()` / `isinstance()` 类型判断
- 转义与引号、`input()` 输入（默认返回字符串，相关代码为注释形式）
- 算术运算：`/` 除法与 `//` 整除的区别
- 分支语句：
  - `if / elif / else`：三角形存在性判断及等边、等腰、普通三角形分类（注释形式）
  - `match...case`：简易计算器，含 `case "/" if b != 0` 的守卫条件（注释形式）
- 循环语句：
  - `for` + `range()`：1~100 累加求和
  - 嵌套 `for`：打印九九乘法表
  - `while True` + `break`：配合 `random.randint()` 的猜数字小游戏

### 数据容器/demo2.py — 列表 list

- 常用方法（注释形式）：`append` 追加、`insert` 插入、`pop` 按索引删除、`remove` 按值删除、`reverse` 反转、`sort` 排序
- 索引取值：`list[0]` 最小值、`list[-1]` 最大值，`sum()/len()` 求平均值
- 综合练习：
  - 合并两个列表并去除重复元素（保持原有顺序）
  - 随机生成 20 个 1~10 的数，筛选出偶数并求平方

### 数据容器/demo3.py — 字符串 str

- 下标访问与切片：`s[2]`、`s[0:5:1]`、`s[-1:-6:-1]`（负数步长反向切片）
- 常用方法：`find` 查找子串下标（找不到返回 -1）、`count` 统计出现次数、`upper` 转大写、`lower` 转小写、`replace` 替换子串

### 数据容器/demo4.py — 元组 tuple

- 元组是不可修改的序列：`t1[0]`、`t1[-1]` 索引取值，`t1[0:5:1]` 切片
- `count()` 统计元素出现次数、`index()` 获取元素首次出现的下标
- 组包与解包（注释形式），含 `*x, y = a` 的星号解包
- 交换变量值：`a, b, c = c, a, b`

### 数据容器/demo5.py — 集合 set

- 集合的创建、`add` 添加、`remove` 删除，以及用 `set()` 对列表去重
- 综合案例（选修课名单统计）：
  - `&` 交集：同时选修两门课、同时选修四门课的学生
  - `-` 差集：选修足球但未选修篮球的学生
  - 拼接多个集合后用 `count()` 统计每个学生选修的课程数量

### 数据容器/demo6.py — 字典 dict

- 字典的创建、按键取值与改值、`items()` 遍历键值对
- 综合案例（购物车管理系统）：`while True` + `match...case` 菜单，实现添加、修改、删除、查询商品与退出，数据以嵌套字典 `{商品名: {"price": ..., "quantity": ...}}` 存储

### 函数/function1.py — 函数

- 函数定义与调用，`return` 返回多个值（以元组形式）
- 函数之间的调用
- 可变参数：`*args` 封装位置参数，`**kwargs` 封装关键字参数
- 匿名函数 `lambda`，递归函数（`jc()` 计算阶乘）
- 综合案例（订单金额计算）：根据商品名、价格、数量及优惠券、积分抵扣、运费计算订单总金额，规则为商品总价满 5000 才可使用优惠券与积分、100 积分抵扣 1 元

### 类练习/class_student.py — 类与对象

- 定义 `student` 类，`__init__` 中保存姓名、语文、数学、英语四个属性
- `__str__` 定义打印格式：`姓名:张三|语文:85|数学:90|英语:88|总分:263`
- `update()` 用默认参数 `None` 实现按需修改单科成绩（传 `None` 表示不改该科）
- `if __name__ == "__main__"` 中添加自测代码

### 类练习/class1.py — 面向对象综合案例（教务管理系统）

- 定义 `jiaowu` 类，用列表 `students` 保存所有学生对象
- `input_score()` 封装成绩输入校验：非整数抛 `ValueError` 时提示并重新输入，且限制在 0~100 分
- 五个功能，均按"输入姓名 → 查找学生 → 处理 → 提示结果"的流程实现：
  - `add_student()` 添加学生（姓名重复则不添加）
  - `update_student()` 修改成绩（先显示当前成绩）
  - `delete_student()` 删除学生（需输入 `yes` 二次确认）
  - `look()` 查询指定学生成绩
  - `show_all()` 展示全部学生成绩（列表为空时给出提示）
- `run()` 用 `while True` + `match...case` 实现控制台菜单，并捕获 `KeyboardInterrupt` / `EOFError` 优雅退出

### json解析/

- `aa.py`：用 `input()` 录入姓名和年龄组成字典，`json.dumps(user, ensure_ascii=False)` 序列化后由 `Path.write_text()` 写入 `ab.json`（`ensure_ascii=False` 保证中文不被转义成 `\uXXXX`）
- `bb.py`：`Path.read_text()` 读取 `ab.json`，用 `json.loads()` 反序列化后打印
- `combine.py`：读写逻辑合并，`path.exists()` 判断文件是否存在——存在则调用 `read()` 读取，不存在则调用 `write()` 写入
- `ab.json`：示例数据文件，内容形如 `{"name": "1", "age": 1}`

### request库/get.py — GET 请求

- 基于 `requests` 调用和风天气 API，用 f-string 拼接域名，把 `params` 与 `headers` 分开传递
- `get_city_id()`：请求城市搜索接口 `geo/v2/city/lookup`，从返回的 `location[0]` 中取出城市 `id`；接口返回码不是 `200` 时提示"没找到城市"
- `get_weather(city_id)`：请求实时天气接口 `v7/weather/now`，打印温度、体感温度、天气、风向，并返回 `re['now']` 整块字典供其他脚本复用
- 逐个捕获异常：`ConnectTimeout`、`Timeout`、`HTTPError`（配合 `raise_for_status()`）、`KeyError`（返回 JSON 缺少字段）、以及兜底的 `Exception`
- `if __name__ == "__main__"` 中串联两个函数，并捕获 `KeyboardInterrupt` 处理手动退出

### request库/post.py — POST 请求

- `from get import get_city_id, get_weather` 复用 `get.py` 的取数逻辑，再把天气数据交给 DeepSeek 生成口语化天气播报
- 请求 `https://api.deepseek.com/v1/chat/completions`，用 `Authorization: Bearer <key>` 认证
- 请求体 `messages` 分两条：
  - `system`：约定角色为天气播报助手，说明 `question` 字典各字段含义，并给出四条规则——完整展示全部天气信息、结合天气给出生活建议、语言简洁口语化不输出原始 JSON、严禁编造数据
  - `user`：把温度、体感温度、天气、风向、风速、湿度拼成文本传入
- 用 `requests.post(url, json=body, ...)` 发送（`json=` 自动序列化并设置 `Content-Type`），设置 `timeout=20`
- 从 `r["choices"][0]["message"]["content"]` 取出模型回复并打印，异常处理比 `get.py` 多捕获一个 `ConnectionError`

## 运行方式

`demo1.py`、`数据容器/`、`函数/`、`类练习/` 没有相对路径依赖，可以在任意目录运行：

```bash
cd "py基础代码练习"
python demo1.py
python "数据容器/demo2.py"
python "数据容器/demo3.py"
python "数据容器/demo4.py"
python "数据容器/demo5.py"
python "数据容器/demo6.py"
python "函数/function1.py"
python "类练习/class1.py"
```

`json解析/` 和 `request库/` 用了相对路径和同目录导入，必须先 `cd` 进对应目录：

```bash
cd "py基础代码练习/json解析"
python aa.py
python bb.py
python combine.py

cd "../request库"
python get.py
python post.py
```

> 提示：`demo1.py` 末尾的猜数字游戏、`demo6.py` 的购物车菜单、`class1.py` 的教务菜单、`aa.py` 和 `combine.py` 的姓名年龄录入都需要手动输入；`demo1.py` 需猜中答案后才会结束，其余程序用 `Ctrl+C` 或菜单里的退出项结束。

## 依赖说明

- Python 3.10+（`demo1.py`、`数据容器/demo6.py`、`类练习/class1.py` 使用了 `match...case`）
- 除 `request库/` 外全部只用标准库：`random`、`pathlib`、`json`
- `request库/` 需要 `requests`：

```bash
pip install requests
```

`requirements.txt` 是 `pip freeze` 导出的完整依赖快照，其中 `certifi`、`charset-normalizer`、`idna`、`urllib3` 是 `requests` 的间接依赖，只有 `requests==2.34.2` 是本目录直接 import 的。

## 使用前准备

`request库/` 中两处密钥在仓库里都用 `*****` 占位，跑之前需要替换成自己的：

- `get.py`：两处 `params` 里的 `"key"`，填和风天气的 API Key
- `post.py`：`key = "sk-*******"`，填 DeepSeek 的 API Key

请勿把真实密钥提交到仓库。

## 待修复问题

- `数据容器/demo6.py`：`buy` 字典定义在 `while` 循环内部，每轮循环都会重置，导致添加或修改的商品无法保留到下一轮操作，把它移到循环外即可正常保存数据。
- `函数/function1.py`：`money()` 中积分按整百折算后的结果 `points1` 没有被使用，返回时仍使用原始积分 `points`，与注释中的抵扣规则不一致。
- `json解析/combine.py`：`write()` 里写的是 `contents = json.dump(user, ensure_ascii=False)`，`json.dump()` 需要传入文件对象且不返回字符串，这里应改为 `json.dumps()`；同时 `read()` 取出 `user` 后没有 `print()`，读取成功时屏幕上不会有任何输出。
- `json解析/combine.py`：顶部 `from py基础代码练习.json解析.aa import user, contents` 会在导入时执行 `aa.py` 的顶层输入语句，而 `combine.py` 自己已经定义了 `write()` / `read()`，这行导入实际未被使用，可以删除。
- `request库/post.py`：`city_id = get_city_id()` 拿到的是 `(城市id, 标志位)` 元组，而 `get_city_id()` 在找不到城市时会返回 `(None, 0)`，所以这里既要把元组解包（参考 `get.py` 的 `city_id, flag = get_city_id()`），也要判断标志位，否则城市查询失败时会继续用 `None` 当城市 id 请求天气。
- `request库/post.py`：`body` 中 `"model"` 为 `deepseek-flash`，与 `deepseek-chat` 等常见命名不同，实际调用前需确认该模型名可用。
- `requirements.txt`：文件是 UTF-16 编码（Windows 下用 PowerShell 重定向 `pip freeze > requirements.txt` 会产生这种编码），应转存为 UTF-8，否则在 Linux/macOS 或部分工具里读取会乱码；文件里的 `Student==0.0.1` 本目录代码并未用到，确认无用后可删除。
