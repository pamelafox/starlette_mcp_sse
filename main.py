import uvicorn
from starlette.applications import Starlette
from routes import routes

# Create Starlette application
app = Starlette(
    debug=True,
    routes=routes,
)

if __name__ == "__main__":
    """Start the Starlette server"""
    uvicorn.run(app, host="0.0.0.0", port=8000)
