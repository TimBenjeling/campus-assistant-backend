# Campus Assistant Backend

面向高校场景的智能体 AIGC 后端原型，提供课堂互动助手、科研文献分析工具、校园智能服务等能力的 API 模板。基于 FastAPI 构建，便于快速对接大模型或校内数据源。

## 功能概览
- **课堂互动助手**：为课堂提问生成讨论思路、追问和互动活动建议。
- **科研文献分析**：对论文题目与摘要生成结构化概要、关键术语与后续阅读步骤。
- **校园智能服务**：根据意图草拟行动计划并列出可用资源，方便集成地图、课表或办事指南数据。

## 快速开始
1. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
2. 启动开发服务器：
   ```bash
   uvicorn app.main:app --reload
   ```
3. 访问 `http://localhost:8000/docs` 查看交互式 API 文档。

## API 概要
- `GET /health`：健康检查。
- `POST /classroom/ask`：输入 `question` 与可选 `course`，返回摘要、追问列表、互动建议。
- `POST /research/summarize`：输入论文 `title` 与 `abstract`，返回概要、关键术语、后续步骤。
- `POST /campus/service`：输入 `intent` 与可选 `detail`，返回行动计划和资源列表。

## 开发提示
- 当前返回内容为示例提示，可替换为大模型调用结果。
- 建议在 `app/main.py` 中扩展依赖注入、鉴权、日志等中间件以适配生产环境。
