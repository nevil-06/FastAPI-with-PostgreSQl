from fastapi import FastAPI
from user.routes import userRouter
from competition.routes import compRouter
from entry.entryRoutes import entryRouter


app = FastAPI()


app.include_router(userRouter)
app.include_router(compRouter)
app.include_router(entryRouter)

