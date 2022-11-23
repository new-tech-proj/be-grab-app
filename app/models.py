from typing import List
from datetime import datetime

from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, String, DateTime, Boolean, ARRAY
from sqlalchemy.sql import func

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, autoincrement="auto", primary_key=True, nullable=False)
    username = Column(String(100), nullable=False, unique=True)
    hashed_password = Column(String(128), nullable=False, unique=True)
    created_date = Column(DateTime, server_default=func.now())
    full_name = Column(String(100))
    address = Column(String(128))
    phone_number = Column(String(12))
    gender = Column(Boolean, default=False)

    def __init__(
        self,
        username: str,
        hashed_password: str,
        full_name: str,
        address: str,
        phone_number: str,
        created_date: DateTime = datetime.now(),
        gender: bool = False
    ):

        self.username = username
        self.hashed_password = hashed_password
        self.created_date = created_date
        self.full_name = full_name
        self.address = address
        self.phone_number = phone_number
        self.gender = gender

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
    created_date = Column(DateTime, server_default=func.now())
    last_modified_date = Column(DateTime, server_default=func.now())
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
        return "Post<(author_id='%s', title='%s', desc='%s', images='%s', created_date='%s', last_modified_date='%s', status='%s')>" % (
            self.author_id,
            self.title,
            self.desc,
            self.images,
            self.created_date,
            self.last_modified_date,
            self.status
        )