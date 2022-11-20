from typing import List
from datetime import datetime

from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, String, DateTime, Boolean, ARRAY

from app.database import Base
from passlib.context import CryptContext

from typing import Union

from pydantic import BaseModel, EmailStr


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, autoincrement="auto", primary_key=True, nullable=False)
    username = Column(String(32), nullable=False, unique=True)
    hashed_password = Column(String(128), nullable=False, unique=True)
    created_date = Column(DateTime, default=datetime.now())
    full_name = Column(String(64))
    address = Column(String(128))
    phone_number = Column(String(12))
    gender = Column(Boolean, default=False)

    def __init__(
        self,
        username: str,
        password: str,
        full_name: str,
        address: str,
        phone_number: str,
        created_date: DateTime = datetime.now(),
        gender: bool = False
    ):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

        self.username = username
        self.hashed_password = self.get_hash_password(password)
        self.created_date = created_date
        self.full_name = full_name
        self.address = address
        self.phone_number = phone_number
        self.gender = gender

    def verify_password(self, plain_password: str):
        return self.pwd_context.verify(plain_password, self.hashed_password)
    
    def get_hash_password(self, password: str):
        return self.pwd_context.hash(password)

    def __repr__(self) -> str:
        return "<User(username='%s', hashed_password='%s', full_name='%s', address='%s', phone_number='%s', created_date='%s', gender='%s')>" % (
            self.username,
            self.hashed_password,
            self.full_name,
            self.address,
            self.phone_number,
            self.created_date,
            self.gender
        )


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, autoincrement="auto", primary_key=True, nullable=False, index=True)
    author_id = Column(Integer, ForeignKey("users.id"), index=True)
    title = Column(String(128), nullable=False)
    desc = Column(String(4096), nullable=False)
    images = Column(ARRAY(String))
    created_date = Column(DateTime, default=datetime.now())
    last_modified_date = Column(DateTime, onupdate=datetime.now())
    status = Column(Boolean, default=False)

    def __init__(
        self,
        author_id: int,
        title: str,
        desc: str,
        images: List[str],
        created_date: DateTime = datetime.now(),
        last_modified_date: DateTime = datetime.now(),
        status: bool = False,
    ):
        self.author_id = author_id
        self.title = title
        self.desc = desc
        self.images = images
        self.created_date = created_date
        self.last_modified_date = last_modified_date
        self.status = status

    def __repr__(self):
        return "Post<(user_id='%s', title='%s', desc='%s', images='%s', created_date='%s', last_modified_date='%s', status='%s')>" % (
            self.user_id,
            self.title,
            self.desc,
            self.images,
            self.created_date,
            self.last_modified_date,
            self.status
        )

class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float

class Response(BaseModel):
    status_code: str
    status_msg: str
    data: str
    
class Request(BaseModel):
    email: EmailStr
    password: str
    phone_number: str
    address: str
    
# class SignUP()

