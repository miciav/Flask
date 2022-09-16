from typing import List
from pydantic import BaseModel

"""
This file contains the definitions of DATA Transfer Objects that in OpenAPI are called Schemas
"""

class BlogBase(BaseModel):
    title: str
    body: str


class Blog(BlogBase):
    class Config():
        orm_mode = True


class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    name: str
    email: str
    id: int
    blogs: List[Blog] = []

    class Config():
        orm_mode = True


class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser

    class Config():
        orm_mode = True
