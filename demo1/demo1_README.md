# demo1 — 实时天气查询与 AI 播报

## 项目简介

输入城市名称，调用和风天气 API 换取城市 ID 并查询实时天气，再交给 DeepSeek 大模型生成一段口语化的天气播报与生活建议。

## 功能

- 输入城市名，调用和风天气 GeoAPI 城市搜索接口换取城市 ID
- 按城市 ID 查询实时天气，提取温度、体感温度、天气状况、风向、风速、湿度六项数据
- 把天气数据交给 DeepSeek，生成口语化播报与「适合做什么、不建议做什么」的生活建议
- 网络异常分类提示：连接超时、请求超时、读取超时、连接错误、HTTP 错误逐类给提示，不直接崩溃
- 业务错误码判断：HTTP 200 不代表业务成功，额外校验响应体的 `code` 字段
- 城市不存在按正常分支处理，提示「未找到城市」后退出，不抛异常
- Ctrl+C 优雅退出提示

## 技术栈

- Python 3.10+ / requests 2.34.2
- 和风天气 API：GeoAPI 城市搜索 `geo/v2/city/lookup`、实时天气 `v7/weather/now`
- DeepSeek API：`/v1/chat/completions`，Bearer Token 认证

## 系统架构

```
用户输入城市名
      │
      ▼
  get_city_id()   ──GET──▶  和风天气 geo/v2/city/lookup
      │                              │
      │◀──────城市 ID + 状态标志──────┘
      ▼
  get_weather(id) ──GET──▶  和风天气 v7/weather/now
      │                              │
      │◀──────── 天气字典 ───────────┘
      ▼
suggest_weather(weather) ──POST──▶ DeepSeek chat/completions
      │                                      │
      ▼◀──────── 口语化播报文本 ─────────────┘
   打印输出
```

> 架构图待补充。

## 项目结构

```
demo1/
├── demo.py             # 主程序：城市查询、天气请求、大模型播报与异常处理
├── requirements.txt    # 依赖清单
├── demo1_README.md     # 项目说明文档
├── images/
│   └── run-result.png  # 运行效果截图
└── venv/               # 本地虚拟环境，已在 .gitignore 中忽略
```

`demo.py` 的函数划分：

- `get_city_id()` — 城市名换城市 ID，返回 `(城市 ID, 状态标志)`
- `get_weather(id)` — 按城市 ID 查实时天气，返回天气字典或 `None`
- `suggest_weather(weather)` — 调用 DeepSeek 生成播报文本并打印

## 核心代码

**1）城市 ID 换取：状态标志代替异常**

```python
c = r["location"][0]
return c["id"], 1        # 成功
# ...
return None, 0           # 失败，由调用方决定是否继续
```

用返回值携带状态标志，而不是到处抛异常，主流程更线性易读。

**2）两道判断：HTTP 状态码 + 业务 code**

```python
if re.status_code == 400:          # 城市名无法识别
    print("未找到城市")
    return None, 0
if re.status_code != 200:
    print(f"HTTP错误,状态码:{re.status_code}")
    return None, 0
r = re.json()
if r.get("code") != "200":         # HTTP 200 不代表业务成功
    print("未找到城市")
    return None, 0
```

**3）`raise_for_status()` 省去逐项判断状态码**

```python
re = requests.get(weather_url, headers=headers, params=params, timeout=5)
re.raise_for_status()              # 非 2xx 直接抛 HTTPError
```

**4）分层捕获异常**

```python
except requests.exceptions.ConnectTimeout:   # 连接超时
except requests.exceptions.Timeout:          # 请求超时
except requests.exceptions.HTTPError as e:   # 4xx / 5xx
except requests.exceptions.RequestException as e:
except Exception as e:                       # 兜底
```

**5）大模型请求体：`system` 约定规则 + `user` 传数据**

```python
body = {
    "model": "deepseek-flash",
    "messages": [
        {"role": "system", "content": "你是专业天气播报助手……"},  # 字段说明 + 四条任务规则
        {"role": "user",   "content": f"温度：{weather['temp']}……"},
    ],
}
re = requests.post(url, headers=headers, json=body, timeout=20)   # 超时单独放宽
print(re.json()["choices"][0]["message"]["content"])
```

`system` 里约定了四条规则：完整展示全部天气信息、结合天气给生活建议、语言简洁口语化且不输出原始 JSON、严禁编造数据。

## 遇到的问题

1. **外层 HTTP 200，但取 `r["location"][0]` 时字段不存在而报错** → 和风天气把真正的结果码放在响应体的 `code` 字段里，城市名写错时 HTTP 层依然是 200 → 改成两道判断：先看 HTTP 状态码，再看业务 `code`，两层都通过才继续。

2. **城市名拼错时程序报错退出** → 把「查不到城市」当成异常处理了，但它其实是预期内会发生的正常情况 → `400` 状态码与业务码非 200 收敛到同一分支，提示「未找到城市」并返回 `(None, 0)`，由调用方按状态标志决定是否继续。

3. **大模型请求总是中断，程序走到「读取超时」分支退出** → 模型接口的 `timeout` 沿用了和天气接口相近的量级，而普通接口返回一个 JSON 很快，模型要逐字生成整段回复，耗时完全不是一个量级 → 模型接口 `timeout` 单独放宽到 20 秒，天气接口保持 5 秒不变。

4. **出错时只能看到「未知错误」，分不清是网络断了、超时了还是密钥错了** → 只写了一个 `except Exception` 兜底 → 按范围从小到大分层捕获 `ConnectTimeout` / `Timeout` / `ReadTimeout` / `HTTPError` / `ConnectionError` / `RequestException`，最后用 `Exception` 兜底；同时用 `raise_for_status()` 把 4xx、5xx 主动转成异常。

5. **程序停在「请输入城市名称」那一步时按 Ctrl+C 接不住，仍甩 traceback** → 主流程的 `try / except KeyboardInterrupt` 盖不住 `get_city_id()`，而这一步内部正有 `input()` 阻塞等待输入 → 需把取城市 ID 也放进 `try` 里（当前代码仍是待修状态）。

## 部署

**1. 克隆仓库**

```bash
git clone https://github.com/kittio0/python_study.git
cd python_study/demo1
```

**2. 创建虚拟环境并安装依赖**

```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS / Linux
pip install -r requirements.txt
```

**3. 配置密钥**

编辑 `demo.py`，把三处 `******` 占位符替换为自己的 Key：

| 位置 | 用途 |
| --- | --- |
| `key` | DeepSeek API Key |
| `get_city_id()` 中的 `params["key"]` | 和风天气 API Key |
| `get_weather()` 中的 `params["key"]` | 和风天气 API Key |

同时确认 `host` 是和风天气控制台分配给自己的专属域名，换账号后需同步修改。

> ⚠️ **密钥不要上传到 Git 仓库。** 写在源码里一旦提交，密钥就会永久留在提交历史中。

**4. 运行**

```bash
python demo.py
```

按提示输入城市名称即可。

## 演示

输入「青岛」，终端输出实时天气数据与大模型生成的口语化播报：

![运行效果：输入青岛后输出实时天气与 AI 播报](images/run-result.png)
