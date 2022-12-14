from fastapi import FastAPI
from app.blog import user_router, blog_router, Base, engine

app = FastAPI()
app.include_router(user_router)
app.include_router(blog_router)


@app.on_event("startup")
async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
