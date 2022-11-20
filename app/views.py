from app import app


@app.get("/")
def index():
    return "Hello, world!"