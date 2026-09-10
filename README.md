# python_study

Python 基础语法学习仓库，记录学习过程中的代码练习，目录按知识点划分。

## 目录结构

```
python_study/
└── py基础代码练习/
    ├── demo1.py          # 基础语法、流程控制、循环
    └── 数据容器/
        ├── demo2.py      # 列表（list）操作
        └── demo3.py      # 字符串（str）操作
```

## 内容说明

### py基础代码练习/demo1.py — 基础语法与流程控制

- 变量定义与多变量赋值、`print` 输出、`type()` / `isinstance()` 类型判断
- 转义与引号、`input()` 输入（默认返回字符串）
- 算术运算：`/` 除法与 `//` 整除的区别
- 分支语句：
  - `if / elif / else`：三角形存在性判断及等边、等腰、普通三角形分类（注释形式）
  - `match...case`：简易计算器，含 `case "/" if b != 0` 的守卫条件（注释形式）
- 循环语句：
  - `for` + `range()`：1~100 累加求和
  - 嵌套 `for`：打印九九乘法表
  - `while True` + `break`：配合 `random.randint()` 的猜数字小游戏

### py基础代码练习/数据容器/demo2.py — 列表 list

- 常用方法（注释形式）：`append` 追加、`insert` 插入、`pop` 按索引删除、`remove` 按值删除、`reverse` 反转、`sort` 排序
- 索引取值：`list[0]` 最小值、`list[-1]` 最大值，`sum()/len()` 求平均值
- 综合练习：
  - 合并两个列表并去除重复元素
  - 随机生成 20 个数，筛选出偶数并求平方

### py基础代码练习/数据容器/demo3.py — 字符串 str

- 下标访问与切片：`s[2]`、`s[0:5:1]`、`s[-1:-6:-1]`（负数步长反向切片）
- 常用方法：`find` 查找子串下标（找不到返回 -1）、`count` 统计出现次数、`upper` 转大写、`lower` 转小写、`replace` 替换子串

## 运行环境

- Python 3.10+（`demo1.py` 中使用了 `match...case` 语法）
- 虚拟环境目录为 `.venv`

## 运行方式

```bash
python "py基础代码练习/demo1.py"
python "py基础代码练习/数据容器/demo2.py"
python "py基础代码练习/数据容器/demo3.py"
```

> 提示：`demo1.py` 中运行时需要手动输入的部分（`input()`、猜数字游戏）默认取消注释后会阻塞在输入等待，按提示输入即可。
