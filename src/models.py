import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

# User, Post, Comment, Like, hashtags, save, page_surfing

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    age = Column(Integer, nullable=False)
    email = Column(String(250), nullable=False)
   

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    caption = Column(String(250))
    location = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    def to_dict(self):
        return {}

class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True)
    content_post = relationship(Post)
    likes_id = Column(Integer, ForeignKey('user.id'))
    responses_id = Column(String(250), ForeignKey('user.id'))

class Like(Base):
    __tablename__ = "like"
    id = Column(Integer, primary_key=True)
    like_post = relationship(Post)
    like_by_user = Column(Integer, ForeignKey('post.id'))
    like_id = relationship(Post)

class Hashtag(Base):
    __tablename__ = "hashtag"
    id = Column(Integer, primary_key=True)
    depiction = Column(String(250), nullable=False)
    hashtag_parent = relationship(Post)
    created_by_user = Column(String(250), ForeignKey('post.id'))
    like_id = relationship(Post)

class Save(Base):
    __tablename__ = "save"
    id = Column(Integer, primary_key=True)
    save_post = relationship(Post)
    saved_by_user = Column(Integer, ForeignKey('post.id'))
    save_id = relationship(Post)
    

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')