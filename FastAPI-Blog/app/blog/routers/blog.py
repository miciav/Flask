from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy import select

from app.blog.routers import schemas
from app.blog.db import models
from app.blog.db.sessionUtils import get_session
from sqlalchemy.ext.asyncio import AsyncSession

blog_router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)


@blog_router.get('/', response_model=List[schemas.ShowBlog])
async def all_blogs(db: AsyncSession = Depends(get_session)):
    """
    Get all blog entries
    """
    results = await db.execute(select(models.Blog))
    blogs = results.scalars().all()
    return blogs


@blog_router.post('/', status_code=status.HTTP_201_CREATED)
async def create(request: schemas.Blog, session: AsyncSession = Depends(get_session)):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    session.add(new_blog)
    await session.commit()
    await session.refresh(new_blog)
    return new_blog


@blog_router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy(id: int, session: AsyncSession = Depends(get_session)):
    results = await session.execute(select(models.Blog).where(models.Blog.id == id))
    blog = results.scalars(0)
    # blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")

    blog.delete(synchronize_session=False)
    await session.commit()
    return 'done'


@blog_router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
async def update(id: int, request: schemas.Blog, session: AsyncSession = Depends(get_session)):
    results = await session.execute(select(models.Blog).where(models.Blog.id == id))
    blog = results.scalars(0)
    # blog = session.query(models.Blog).filter(models.Blog.id == id)

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")

    blog.update(request)
    await session.commit()
    return 'updated'


@blog_router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
async def show(id: int, session: AsyncSession = Depends(get_session)):
    results = await session.execute(select(models.Blog).where(models.Blog.id == id))
    blog = results.scalars(0)
    # blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not available")
    return blog
