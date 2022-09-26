from typing import List, Union, Optional
from pydantic import BaseModel, validator

"""
This file contains the definitions of DATA Transfer Objects that in OpenAPI are called Schemas
"""


class BlogBase(BaseModel):
    title: str
    body: str
    user_id: int


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
    blogs: Optional[List[Blog]] = None

    class Config:
        orm_mode = True


class ShowUserLight(BaseModel):
    name: str
    email: str
    id: int

    class Config:
        orm_mode = True


class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUserLight

    class Config:
        orm_mode = True
