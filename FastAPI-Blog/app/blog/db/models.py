from sqlalchemy import Column, Integer, String, ForeignKey, inspect, Table
from app.blog.db import Base
from sqlalchemy.orm import relationship



class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    creator = relationship("User", back_populates="blogs")
    __mapper_args__ = {"eager_defaults": True}

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    blogs = relationship('Blog', back_populates="creator")


