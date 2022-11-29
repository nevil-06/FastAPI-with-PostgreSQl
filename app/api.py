from fastapi import FastAPI
from user.userRoutes import userRouter
from competition.compRoutes import compRouter
from entry.entryRoutes import entryRouter


app = FastAPI()


app.include_router(userRouter)
app.include_router(compRouter)
app.include_router(entryRouter)

