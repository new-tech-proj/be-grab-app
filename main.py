import os
import uvicorn

from app import app


if __name__ == "__main__":
    config = uvicorn.Config(
        app=app,
        host="127.0.0.1",
        port=os.getenv("PORT", default=5000),
        log_level="info"
    )
    server = uvicorn.Server(config)
    server.run()