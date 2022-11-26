from fastapi import FastAPI

app = FastAPI()

success_status = 0
fail_status = 1

from app.views import *