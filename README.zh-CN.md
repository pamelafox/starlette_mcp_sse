# Starlette MCP SSE

<p align="center">
  <a href="/README.md">English</a> | <strong>简体中文</strong>
</p>

这是一个使用 Starlette 框架实现的服务器推送事件（SSE）项目，集成了 [模型上下文协议 (MCP)](https://modelcontextprotocol.io/)。

## 什么是 MCP？

[模型上下文协议 (MCP)](https://modelcontextprotocol.io/) 是一个开放标准，使 AI 模型能够与外部工具和数据源交互。MCP 解决了 AI 开发中的几个关键挑战：

- **上下文限制**：允许模型访问超出其训练数据的最新信息
- **工具集成**：为模型使用外部工具和 API 提供标准化方式
- **互操作性**：在不同 AI 模型和工具之间创建通用接口
- **可扩展性**：便于在无需重新训练的情况下为 AI 系统添加新功能

本项目展示了如何在 Starlette Web 应用中使用服务器推送事件 (SSE) 实现 MCP。

## 描述

本项目展示了如何使用 Starlette 框架实现服务器推送事件 (SSE)，同时集成模型上下文协议 (MCP) 功能。其核心特点是将 MCP 的 SSE 功能无缝集成到一个包含自定义路由的完整 Starlette Web 应用中。

## 功能

- 基于 MCP 的服务器推送事件 (SSE) 实现
- 与 Starlette 框架集成，支持自定义路由
- 统一 Web 应用，同时支持 MCP 和标准 Web 端点
- 可自定义的路由结构
- MCP 功能与 Web 功能的清晰分离

## 架构

本项目展示了一个模块化架构，包括：

1. 将 MCP SSE 端点（`/sse` 和 `/messages/`）集成到 Starlette 应用中
2. 提供标准 Web 路由（`/`、`/about`、`/status`、`/docs`）
3. 展示如何保持 MCP 功能与 Web 路由的分离

## 安装与使用选项

### 前置条件

安装 [UV 包管理器](https://docs.astral.sh/uv/) - 一个用 Rust 编写的快速 Python 包安装工具：

```cmd
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 选项 1：无需安装直接运行

使用 UV 的执行工具直接运行应用，无需克隆仓库：

```cmd
uvx --from git+https://github.com/panz2018/starlette_mcp_sse.git start
```

### 选项 2：完整安装

#### 创建虚拟环境

为项目创建一个隔离的 Python 环境：

```cmd
uv venv
```

#### 激活虚拟环境

激活虚拟环境以使用它：

```cmd
.venv\Scripts\activate
```

#### 安装依赖

安装所有必需的包：

```cmd
uv pip install -r pyproject.toml
```

#### 启动集成服务器

启动集成了 MCP SSE 功能的 Starlette 服务器：

```cmd
python src/server.py
```

或

```cmd
uv run start
```

### 可用端点

启动服务器后（使用选项 1 或选项 2），以下端点将可用：

- 主服务器：http://localhost:8000
- 标准 Web 路由：
  - 主页：http://localhost:8000/
  - 关于页面：http://localhost:8000/about
  - 状态 API：http://localhost:8000/status
  - 文档：http://localhost:8000/docs
- MCP SSE 端点：
  - SSE 端点：http://localhost:8000/sse
  - 消息发布：http://localhost:8000/messages/

### 使用 MCP Inspector 调试

使用 MCP Inspector 测试和调试 MCP 功能：

```cmd
mcp dev ./src/weather.py
```

### 连接到 MCP Inspector

1. 打开 MCP Inspector：http://localhost:5173
2. 配置连接：
   - 设置传输类型为 `SSE`
   - 输入 URL：http://localhost:8000/sse
   - 点击 `Connect`

### 测试功能

1. 导航到 `Tools` 部分
2. 点击 `List Tools` 查看可用功能：
   - `get_alerts`：获取天气警报
   - `get_forecast`：获取天气预报
3. 选择一个功能
4. 输入所需参数
5. 点击 `Run Tool` 执行

## 扩展应用

### 添加自定义路由

应用结构便于添加新路由：

1. 在 routes.py 中定义新的路由处理程序
2. 将路由添加到 routes.py 中的路由列表
3. 主应用将自动包含这些路由

### 自定义 MCP 集成

MCP SSE 功能通过以下方式在 server.py 中集成：

- 创建 SSE 传输
- 设置 SSE 处理程序
- 将 MCP 路由添加到 Starlette 应用

## 与 [Continue](https://www.continue.dev/) 集成

要将此 MCP 服务器与 Continue VS Code 扩展一起使用，请在 Continue 设置中添加以下配置：

```json
{
  "experimental": {
    "modelContextProtocolServers": [
      {
        "transport": {
          "name": "weather",
          "type": "sse",
          "url": "http://localhost:8000/sse"
        }
      }
    ]
  }
}
```
