import os
import sys
from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import declarative_base, relationship
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
    comment = relationship(Comment, backref='post')
    media = relationship(Media, backref='post')

class Follower(Base):
    __tablename__ = 'follower'
    user_from_id = Column(Integer, primary_key=True)
    user_to_id = Column(Integer, primary_key=True)
    user = relationship(User, backref='follower')

render_er(Base, 'diagram.png')