from fastapi import FastAPI
from app.user.router import userRouter
from app.competition.router import compRouter
from app.entry.router import entryRouter


app = FastAPI()


app.include_router(userRouter)
app.include_router(compRouter)
app.include_router(entryRouter)
