from blog import models
from blog.database import engine
from blog.routers import blog, user


userRouter = user.userRouter
blogRouter = blog.router

models.Base.metadata.create_all(engine)
