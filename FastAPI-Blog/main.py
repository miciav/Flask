from fastapi import FastAPI
from blog import user_router, blog_router, Base, engine

app = FastAPI()
app.include_router(user_router)
app.include_router(blog_router)

Base.metadata.create_all(engine)

