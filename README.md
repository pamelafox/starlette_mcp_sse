# Starlette MCP SSE

A Server-Sent Events (SSE) implementation using Starlette framework with Model Context Protocol (MCP) integration.

## Description

This project demonstrates how to implement Server-Sent Events (SSE) using the Starlette framework while integrating Model Context Protocol (MCP) functionality. The key feature is the seamless integration of MCP's SSE capabilities within a full-featured Starlette web application that includes custom routes.

## Features

- Server-Sent Events (SSE) implementation with MCP
- Starlette framework integration with custom routes
- Unified web application with both MCP and standard web endpoints
- Customizable route structure
- Clean separation of concerns between MCP and web functionality

## Architecture

This project showcases a modular architecture that:

1. Integrates MCP SSE endpoints (`/sse` and `/messages/`) into a Starlette application
2. Provides standard web routes (`/`, `/about`, `/status`, `/docs`)
3. Demonstrates how to maintain separation between MCP functionality and web routes

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

### Start the Integrated Server

Launch the integrated Starlette server with MCP SSE functionality:

```cmd
python main.py
```

The server will be available at:

- Main server: http://localhost:8000
- Standard web routes:
  - Home page: http://localhost:8000/
  - About page: http://localhost:8000/about
  - Status API: http://localhost:8000/status
  - Documentation: http://localhost:8000/docs
- MCP SSE endpoints:
  - SSE endpoint: http://localhost:8000/sse
  - Message posting: http://localhost:8000/messages/

### Debug with MCP Inspector

For testing and debugging MCP functionality, use the MCP Inspector:

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

## Extending the Application

### Adding Custom Routes

The application structure makes it easy to add new routes:

1. Define new route handlers in routes.py
2. Add routes to the routes list in routes.py
3. The main application will automatically include these routes

### Customizing MCP Integration

The MCP SSE functionality is integrated in main.py through:

- Creating an SSE transport
- Setting up an SSE handler
- Adding MCP routes to the Starlette application

## Integration with [Continue](https://www.continue.dev/)

To use this MCP server with the Continue VS Code extension, add the following configuration to your Continue settings:

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
