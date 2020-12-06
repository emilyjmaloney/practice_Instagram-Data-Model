import os
import sys
from datetime import datetime, timezone
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    id=Column(Integer, primary_key=True)
    name=Column(String(50), nullable=False)
    username=Column(String(30), nullable=False, unique=True)
    password=Column(String(30), nullable=False)
    email_address=Column(String(50), nullable=False, unique=True)
    posts=relationship("Post", backref="author")
    comments=relationship("Comment", backref="author")
    sent_messages=relationship("Message", backref="sender")
    received_messages=relationship("Message", backref="recipient")

class Post(Base):
    __tablename__ = "post"
    id=Column(Integer, primary_key=True)
    user_id=Column(Integer, ForeignKey("user.id"))
    photo_url=Column(String(250))
    caption=Column(String(250))
    date=Column(DateTime())
    comments=relationship("Comment", backref="post")

class Comment(Base):
    __tablename__ = "comment"
    id=Column(Integer, primary_key=True)
    user_id=Column(Integer, ForeignKey("user.id"))
    post_id=Column(Integer, ForeignKey("post.id"))
    text=Column(String(250))
    date=Column(DateTime())

class Message(Base):
    __tablename__ = "message"
    id=Column(Integer, primary_key=True)
    sender_id=Column(Integer, ForeignKey("user.id"))
    recipient_id=Column(Integer, ForeignKey("user.id"))
    text=Column(String(250))
    created_at=Column(DateTime())
    
        # Here we define columns for the table user
    # Notice that each column is also a normal Python instance attribute.
        
# class Address(Base):
#     __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

# ## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')