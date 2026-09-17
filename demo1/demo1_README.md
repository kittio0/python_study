# demo1 — 实时天气查询与 AI 播报

## 1. 项目简介

基于 `requests` 调用和风天气 API 与 DeepSeek 大模型的练习项目。输入城市名称，先换取城市 ID，再查询该城市的实时天气，最后由大模型生成一段口语化的天气播报。

练习到的技术点：

- `requests` 发送 GET / POST 请求，`params` 传参，`json=` 提交请求体
- 解析嵌套 JSON，从多层结构中取值
- 异常处理：连接超时、请求超时、连接失败、HTTP 错误状态码
- 判断接口业务返回码，处理「城市不存在」这类边界场景
- 捕获 `KeyboardInterrupt`，支持 Ctrl+C 优雅退出
- 用函数拆分流程，返回值携带状态标志
- 密钥占位符与 `.gitignore` 忽略规则

## 2. ✨主要功能

- 输入城市名 → 调用和风天气城市搜索接口 → 换取城市 ID
- 按城市 ID 查询实时天气，提取温度、体感温度、天气状况、风向、风速、湿度
- 将天气数据交给 DeepSeek，生成口语化播报与生活建议

异常与边界处理：

- **网络异常**：分别捕获连接超时、读取超时、请求超时、连接错误、HTTP 错误，逐类给出提示
- **业务错误码**：HTTP 状态码为 200 不代表业务成功，额外判断响应体里的 `code` 字段
- **城市不存在**：400 状态码与业务码非 200 均按「未找到城市」处理，返回失败标志而不是继续往下走
- **未知异常**：以 `Exception` 兜底，避免程序直接崩溃
- **中途中止**：捕获 `KeyboardInterrupt`，Ctrl+C 时输出提示后退出

## 3. 📦环境依赖

- Python 3.10+（`requests` 2.34.2 的 `Requires-Python` 为 `>=3.10`）
- 依赖文件：`requirements.txt`

```bash
pip install -r requirements.txt
```

依赖清单（含 `requests` 的间接依赖）：

```
certifi==2026.7.22
charset-normalizer==3.5.1
idna==3.19
requests==2.34.2
urllib3==2.7.0
```

另需自行申请两个 Key：和风天气 API Key、DeepSeek API Key。

## 4. 🚀快速开始

### 克隆仓库

```bash
git clone https://github.com/kittio0/python_study.git
cd python_study/demo1
```

### 创建虚拟环境并安装依赖

```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS / Linux
pip install -r requirements.txt
```

### 配置密钥

编辑 `demo.py`，把三处 `******` 占位符替换为自己的 Key：

| 位置 | 用途 |
| --- | --- |
| `key` | DeepSeek API Key |
| `get_city_id()` 中的 `params["key"]` | 和风天气 API Key |
| `get_weather()` 中的 `params["key"]` | 和风天气 API Key |

同时确认 `host` 是和风天气控制台分配给自己的专属域名，换账号后需同步修改。

> ⚠️ **密钥不要上传到 Git 仓库。** 写在源码里一旦提交，密钥就会永久留在提交历史中，即使后续删除也仍可被翻出。推荐改用环境变量或 `.env` 读取 —— 仓库的 `.gitignore` 已经配置了 `.env` 与 `venv/` 的忽略规则。

### 运行

```
python demo.py
```

按提示输入城市名称即可。

## 5. 📁项目目录结构

```
demo1/
├── demo.py             # 主程序：城市查询、天气请求、大模型播报与异常处理
├── requirements.txt    # 依赖清单
├── demo1_README.md     # 项目说明文档
└── venv/               # 本地虚拟环境，已在 .gitignore 中忽略
```

`demo.py` 的函数划分：

- `get_city_id()` — 城市名换城市 ID，返回 `(城市 ID, 状态标志)`
- `get_weather(id)` — 按城市 ID 查实时天气，返回天气字典或 `None`
- `suggest_weather(weather)` — 调用 DeepSeek 生成播报文本并打印

## 6. 💡开发思考

**1）HTTP 200 不等于请求成功**

最初只判断 `re.status_code == 200`，但和风天气把真正的结果码放在响应体的 `code` 字段里。城市名写错时外层依然是 HTTP 200，代码会继续往下走，直到取 `r["location"][0]` 才发现字段不存在而报错。后来改成两道判断：先看 HTTP 状态码，再看业务 `code`，两层都通过才继续。

**2）城市不存在应当作正常分支，而非异常**

城市名拼错、接口查不到匹配城市，都是预期内会发生的情况，不该让程序报错退出。现在 `400` 状态码和业务码非 200 都收敛到同一个分支，提示「未找到城市」并返回 `(None, 0)`，由调用方根据状态标志决定是否继续。用状态标志而不是抛异常，主流程也更线性易读。

**3）大模型的超时时间必须单独放宽**

最初大模型接口沿用了和天气接口相近的超时值，结果请求还没等模型把整段文本生成完就中断，抛出 `ReadTimeout`，程序直接走到「读取超时」分支退出，表现就是运行失败。原因是普通接口返回一个 JSON 很快，而大模型要逐字生成整段回复，耗时完全不是一个量级。把模型接口的 `timeout` 单独设为 20 秒后正常；天气接口保持 5 秒即可，不必跟着调大。

**4）异常要分类捕获，才知道问题出在哪**

一开始只写一个 `except Exception`，出错时只能看到「未知错误」，分不清是网络断了、超时了还是密钥错了。现在按范围从小到大分层：`ConnectTimeout` / `Timeout` / `ReadTimeout` / `HTTPError` / `ConnectionError` / `RequestException`，最后用 `Exception` 兜底。另外用 `raise_for_status()` 把 4xx、5xx 主动转成异常，省去逐项判断状态码。

**5）Ctrl+C 的退出提示没盖住全部流程**

主流程外面套了 `try / except KeyboardInterrupt`，但 `get_city_id()` 是在这层 `try` 之外调用的，而它内部正有 `input()` 等待输入。所以程序停在「请输入城市名称」那一步时按 Ctrl+C 接不住，仍会甩出 traceback。要彻底解决，需要把取城市 ID 这一步也放进 `try` 里。

**6）密钥从写死改成占位符，但还不够**

代码里的 Key 现在是 `******` 占位符，这样文件可以安全提交到公开仓库。但硬编码本身仍是坏习惯：只要有人替换成真实 Key 后再 `git commit`，密钥就进了提交历史。更稳妥的做法是从环境变量或 `.env` 读取，仓库里已经配好了 `.env` 的忽略规则，改造时不用再动 `.gitignore`。

**7）两个环境相关的小坑**

- `requirements.txt` 是用 PowerShell 的 `>` 重定向导出的 `pip freeze`，文件被写成了 UTF-16 编码，在 Linux、macOS 或部分工具里读出来是乱码。建议在 CMD / Git Bash 下导出，或导出后另存为 UTF-8。
- `venv/` 是从其他目录移动过来的，`Scripts/activate` 里记录的仍是旧路径，激活后会指向一个不存在的目录。这种情况下可以直接用 `venv\Scripts\python.exe demo.py` 运行，或删除 `venv/` 后重建。

## 7. 📄许可证

本项目采用 **MIT License**，可自由使用、修改、分发，需保留版权声明。

> 注：仓库目前尚未添加 `LICENSE` 文件，如需正式采用 MIT 协议，建议补充一份。
