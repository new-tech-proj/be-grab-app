from datetime import datetime
from pydantic import BaseModel

class dtoUser(BaseModel):
    username: str
    hashed_password: str
    full_name: str
    address: str
    phone_number: str
    created_date: datetime
    gender: bool