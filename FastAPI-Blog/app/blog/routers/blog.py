from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy import select, update
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import selectinload

from app.blog.routers import schemas
from app.blog.db import models
from app.blog.db.sessionUtils import get_session
from sqlalchemy.ext.asyncio import AsyncSession

blog_router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)


@blog_router.post('/', status_code=status.HTTP_201_CREATED)
async def create(request: schemas.Blog, session: AsyncSession = Depends(get_session)):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=request.user_id)
    session.add(new_blog)
    try:
        await session.commit()
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {request.user_id} is not available")

    return new_blog


@blog_router.get('/', response_model=List[schemas.ShowBlog])
async def all_blogs(session: AsyncSession = Depends(get_session)):
    """
    Get all blog entries
    """
    results = await session.execute(select(models.Blog).options(selectinload(models.Blog.creator)))
    blogs = results.scalars().all()
    return blogs


@blog_router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
async def show(id: int, session: AsyncSession = Depends(get_session)):
    results = await session.execute(
        select(models.Blog).where(models.Blog.id == id).options(selectinload(models.Blog.creator)))
    blog = results.scalars().first()
    # blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not available")
    return blog


@blog_router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy(id: int, session: AsyncSession = Depends(get_session)):
    results = await session.execute(select(models.Blog)
                                    .where(models.Blog.id == id))
    blog = results.scalar_one_or_none()
    # blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")

    # blog.delete(synchronize_session=False)
    await session.delete(blog)
    await session.commit()
    return 'done'


@blog_router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
async def put(id: int, request: schemas.Blog, session: AsyncSession = Depends(get_session)):
    results = await session.execute(select(models.Blog).where(models.Blog.id == id))
    blog = results.scalar_one_or_none()

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")

    q = update(models.Blog).where(models.Blog.id == id).values(**request.dict())
    results = await session.execute(q)

    await session.commit()
    return 'updated'
