from databases import Database
from sqlalchemy.ext.asyncio import AsyncSession

from app.blog.db import async_session

    # db = session_local()
    # try:
    #     yield db
    # finally:
    #     db.close()


async def get_session():
    async with async_session() as session:
        yield session




