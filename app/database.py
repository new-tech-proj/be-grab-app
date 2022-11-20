from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

from app.settings import DATABASE_URL


engine = create_engine(DATABASE_URL, echo=False)
metadata = MetaData(bind=engine)

session = Session(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()