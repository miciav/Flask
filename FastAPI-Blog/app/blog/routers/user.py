from databases import Database
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.blog.routers import schemas
from app.blog.db import models
from app.blog.db.sessionUtils import get_session
from fastapi import APIRouter, Depends, status, HTTPException
from app.blog.routers.utils import Hash

user_router = APIRouter(
    prefix="/user",
    tags=['Users']
)


@user_router.post('/', response_model=schemas.ShowUser)
async def create_user(request: schemas.User, session: AsyncSession = Depends(get_session)):
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password), blogs=[])
    async with session.begin():
        session.add(new_user)
    await session.commit()
    return new_user


@user_router.get('/{id}', response_model=schemas.ShowUser)
async def get_user(id: int, session: AsyncSession = Depends(get_session)):
    async with session.begin():
        # user = await session.get(models.User, id, populate_existing=True, )
        results = await session.execute(select(models.User).where(models.User.id == id).options(selectinload(models.User.blogs)))
    user = results.scalars().first()
    # user = await session.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} is not available")

    return user
