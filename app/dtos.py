from typing import List
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

class dtoUserLogin(BaseModel):
    username: str
    password: str

class dtoPost(BaseModel):
    author_id: int
    title: str
    desc: str
    images: List[str]
    created_date: datetime
    last_modified_date: datetime
    status: bool
    
class dtoUpdatePost(BaseModel):
    title: str
    desc: str
    images: List[str]
    status: bool