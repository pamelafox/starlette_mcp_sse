from starlette.routing import Route
from starlette.responses import JSONResponse, HTMLResponse, PlainTextResponse
from datetime import datetime


async def homepage(request):
    return HTMLResponse(
        "<h1>Starlette MCP SSE</h1><p>Welcome to the SSE demo with MCP integration.</p>"
    )


async def about(request):
    return PlainTextResponse(
        "About Starlette MCP SSE: A demonstration of Server-Sent Events with Model Context Protocol integration."
    )


async def status(request):
    status_info = {
        "status": "running",
        "server": "Starlette MCP SSE",
        "version": "0.1.0",
        "timestamp": datetime.now().isoformat(),
    }
    return JSONResponse(status_info)


async def docs(request):
    return PlainTextResponse(
        "API Documentation:\n"
        "- GET /sse: Server-Sent Events endpoint\n"
        "- POST /messages: Send messages to be broadcasted\n"
        "- GET /status: Server status information"
    )


routes = [
    Route("/", endpoint=homepage),
    Route("/about", endpoint=about),
    Route("/status", endpoint=status),
    Route("/docs", endpoint=docs),
]
