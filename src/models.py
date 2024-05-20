import os
import sys
from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import declarative_base
from eralchemy2 import render_er

Base = declarative_base()

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    Comment_text = Column(String)
    Author_id = Column(Integer)
    post_id = Column(Integer)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    firstname = Column(String)
    email = Column(String)

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(Enum)
    url = Column(String)
    post_id = Column(Integer)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)

class Follower(Base):
    __tablename__ = 'follower'
    user_from_id = Column(Integer, primary_key=True)
    user_to_id = Column(Integer, primary_key=True)

def to_dict(self):
    return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem generating the diagram")
    raise e