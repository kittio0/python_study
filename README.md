# python_study

- `demo1/` — 天气查询项目：调用和风天气 API 查实时天气，再由 DeepSeek 生成口语化播报
- `py基础代码练习/` — Python 基础语法练习：变量与流程控制、数据容器、函数、类与对象、JSON 读写、网络请求

## 目录结构

```
python_study/
├── demo1/                          # 项目：输入城市名，查实时天气并生成 AI 播报
│   ├── demo.py                     # 主程序：城市查询、天气请求、大模型播报、异常处理
│   ├── requirements.txt            # 依赖清单（requests）
│   ├── demo1_README.md             # 项目说明
│   └── images/run-result.png       # 运行效果截图
│
└── py基础代码练习/                  # 基础语法练习
    ├── basic_README.md             # 练习目录说明
    ├── requirements.txt            # 依赖清单
    ├── demo1.py                    # 基础语法与流程控制
    │
    ├── 数据容器/                    # 五种容器的用法练习
    │   ├── demo2.py                # 列表 list：增删改查、切片、列表推导
    │   ├── demo3.py                # 字符串 str：下标、切片、常用方法
    │   ├── demo4.py                # 元组 tuple：索引切片、组包解包、交换变量
    │   ├── demo5.py                # 集合 set：去重、交并差集（选修课名单统计）
    │   └── demo6.py                # 字典 dict：嵌套字典（购物车管理系统）
    │
    ├── 函数/
    │   └── function1.py            # 函数、可变参数、lambda、递归（订单金额计算）
    │
    ├── 类练习/
    │   ├── class_student.py        # 类与对象：学生类
    │   └── class1.py               # 面向对象综合案例：教务管理系统
    │
    ├── json解析/
    │   ├── aa.py                   # 写入 JSON 文件
    │   ├── bb.py                   # 读取 JSON 文件
    │   ├── combine.py              # 读写合并：文件存在则读，不存在则写
    │   └── ab.json                 # 示例数据文件
    │
    └── request库/
        ├── get.py                  # GET 请求：和风天气城市搜索与实时天气
        └── post.py                 # POST 请求：把天气数据交给 DeepSeek 生成播报
```
