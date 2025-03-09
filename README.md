# Starlette MCP SSE

A Server-Sent Events (SSE) implementation using Starlette framework.

## Description

This project demonstrates how to implement Server-Sent Events (SSE) using the Starlette framework.

## Features

- Server-Sent Events (SSE) implementation
- Starlette framework integration

## Installation

### Prerequisites

Install UV Package Manager - A fast Python package installer written in Rust:

```cmd
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Virtual Environment Setup

Set up an isolated Python environment for the project:

```cmd
uv venv
.venv\Scripts\activate
```

### Install Dependencies

Install all required packages:

```cmd
uv pip install -r pyproject.toml
```

## Quick Start

### Start the MCP Server

Launch the SSE server:

```cmd
python main.py
```

The server will be available at:

- Main server: http://localhost:8000
- SSE endpoint: http://localhost:8000/sse

### Debug with MCP Inspector

For testing and debugging, use the MCP Inspector:

```cmd
mcp dev ./weather.py
```

### Connect to MCP Inspector

1. Open MCP Inspector at http://localhost:5173
2. Configure the connection:
   - Set Transport Type to `SSE`
   - Enter URL: http://localhost:8000/sse
   - Click `Connect`

### Test the Functions

1. Navigate to `Tools` section
2. Click `List Tools` to see available functions:
   - `get_alerts` : Get weather alerts
   - `get_forcast` : Get weather forecast
3. Select a function
4. Enter required parameters
5. Click `Run Tool` to execute
