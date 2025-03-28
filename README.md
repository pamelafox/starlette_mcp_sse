# Starlette MCP SSE

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/pamelafox/starlette_mcp_sse)
[![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/pamelafox/starlette_mcp_sse)

A Server-Sent Events (SSE) implementation using Starlette framework with [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) integration.

This project demonstrates how to implement Server-Sent Events (SSE) using the Starlette framework while integrating Model Context Protocol (MCP) functionality. The key feature is the seamless integration of MCP's SSE capabilities within a full-featured Starlette web application that includes custom routes.

* [What is MCP?](#what-is-mcp)
* [Features](#features)
* [Getting started](#getting-started)
  * [GitHub Codespaces](#github-codespaces)
  * [VS Code Dev Containers](#vs-code-dev-containers)
  * [Local Environment](#local-environment)
* [Deploying](#deploying)
* [Development server](#development-server)

## What is MCP?

The [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) is an open standard that enables AI models to interact with external tools and data sources. MCP solves several key challenges in AI development:

* **Context limitations**: Allows models to access up-to-date information beyond their training data

* **Tool integration**: Provides a standardized way for models to use external tools and APIs

* **Interoperability**: Creates a common interface between different AI models and tools

* **Extensibility**: Makes it easy to add new capabilities to AI systems without retraining

This project demonstrates how to implement MCP using Server-Sent Events (SSE) in a Starlette web application.

## Features

* Server-Sent Events (SSE) implementation with MCP

* Starlette framework integration with custom routes

* Unified web application with both MCP and standard web endpoints

* Customizable route structure

* Clean separation of concerns between MCP and web functionality

* Simple Client that can be used to test the SSE endpoints

## Architecture

This project showcases a modular architecture that:

1. Integrates MCP SSE endpoints (`/sse` and `/messages/`) into a Starlette application
2. Provides standard web routes (`/`, `/about`, `/status`, `/docs`)
3. Demonstrates how to maintain separation between MCP functionality and web routes

## Getting started

You have a few options for getting started with this template.
The quickest way to get started is GitHub Codespaces, since it will setup all the tools for you, but you can also [set it up locally](#local-environment).

### GitHub Codespaces

You can run this template virtually by using GitHub Codespaces. The button will open a web-based VS Code instance in your browser:

1. Open the template (this may take several minutes):

    [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/pamelafox/starlette_mcp_sse)

2. Open a terminal window
3. Continue with the [deploying steps](#deploying)

### VS Code Dev Containers

A related option is VS Code Dev Containers, which will open the project in your local VS Code using the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):

1. Start Docker Desktop (install it if not already installed)
2. Open the project:

    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/pamelafox/starlette_mcp_sse)

3. In the VS Code window that opens, once the project files show up (this may take several minutes), open a terminal window.
4. Continue with the [deploying steps](#deploying)

### Local Environment

If you're not using one of the above options for opening the project, then you'll need to:

1. Make sure the following tools are installed:
    * [Docker Desktop](https://www.docker.com/products/docker-desktop)
    * [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)
    * [Python 3.13](https://www.python.org/downloads/)
    * [UV Package Manager](https://docs.astral.sh/uv/)

2. Clone this repository:

    ```bash
    git clone https://github.com/pamelafox/starlette_mcp_sse.git
    ```

3. Open the project folder

4. Create a [Python virtual environment](https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments) and activate it.

    ```bash
    uv venv
    ```

5. Install the the MCP server packages:

    ```bash
    uv pip install -e mcp_server
    ```

6. Install the MCP client packages:

    ```bash
    uv pip install -e mcp_client
    ```

7. Continue with the [deploying steps](#deploying).

## Deploying

To deploy the application, you can use Docker to create a container image and then deploy it to Azure Container Apps.

## Deploy to Azure

1. Login to Azure:

    ```shell
    az login
    ```

2. Create a resource group:

    ```shell
    az group create --name RESOURCEGROUP --location LOCATION
    ```

3. Create an Azure Container Apps environment:

    ```shell
    az containerapp env create --name CONTAINERAPPSENV --resource-group RESOURCEGROUP --location LOCATION
    ```

4. Run this command to deploy the application to Azure Container Apps:

    ```shell
    az containerapp compose create -g RESOURCEGROUP --environment CONTAINERAPPSENV --compose-file-path docker-compose.yaml
    ```

> [!NOTE]
> Once it deploys, update the SERVER_URL environment variable in the Azure portal to point to the new URL of your deployed application. Then check the Console logs once revision is deployed.
>
> NOTE THAT THIS WILL EXPOSE IT PUBLICLY.

## Development server

### MCP Server

Assuming you've run the steps to [open the project](#getting-started) or [local environment](#local-environment) you can now run the MCP server in your development environment:

Launch the integrated Starlette server with MCP SSE functionality:

```cmd
uv run mcp_server/src/server.py
```

or

```cmd
cd mcp_server
uv run start
```

### MCP Client

To run the MCP client, you can use the following command:

```cmd
uv run mcp_client/src/client.py
```

### Available Endpoints

After starting the server (using either Option 1 or Option 2), the following endpoints will be available:

* Main server: <http://localhost:8000>
* Standard web routes:
  * Home page: <http://localhost:8000/>
  * About page: <http://localhost:8000/about>
  * Status API: <http://localhost:8000/status>
  * Documentation: <http://localhost:8000/docs>
* MCP SSE endpoints:
  * SSE endpoint: <http://localhost:8000/sse>
  * Message posting: <http://localhost:8000/messages/>

### Debug with MCP Inspector

For testing and debugging MCP functionality, use the MCP Inspector:

```cmd
uv run mcp dev mcp_server/src/weather.py
```

### Connect to MCP Inspector

1. Open MCP Inspector at <http://localhost:5173>
2. Configure the connection:
   * Set Transport Type to `SSE`
   * Enter URL: <http://localhost:8000/sse>
   * Click `Connect`

### Test the Functions

1. Navigate to `Tools` section
2. Click `List Tools` to see available functions:
   * `get_alerts` : Get weather alerts
   * `get_forcast` : Get weather forecast
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

The MCP SSE functionality is integrated in server.py through:

* Creating an SSE transport
* Setting up an SSE handler
* Adding MCP routes to the Starlette application

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
