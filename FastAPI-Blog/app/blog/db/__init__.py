from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine

SQLALCHAMY_DATABASE_URL = 'sqlite+aiosqlite:///blog.db'

engine = create_async_engine(SQLALCHAMY_DATABASE_URL, connect_args={"check_same_thread": False})

async_session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()


