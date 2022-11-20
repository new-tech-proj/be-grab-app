from app import app
from fastapi import Response
from app.models import Item, Request
from app.database import session


@app.get("/")
def index():
    return "Hello, world!"

@app.post("/signup")
def test_post(request: Request):
    print(Item)
    return {
        "status_code": "success",
        "status_msg": "Hello post method",
        "data": {
            "thinh": 12000
        }
    }