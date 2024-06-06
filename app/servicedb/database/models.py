from sqlalchemy import Column, Integer, Text, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Posts(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    surname = Column(String(255))
    patronymic = Column(String(255))
    phone = Column(String(255))
    text = Column(String)  # Assuming you want similar to VARCHAR without specifying length
