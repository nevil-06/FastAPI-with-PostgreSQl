from fastapi import FastAPI#,HTTPException

from routes import userRoutes,compRoutes,entryRoutes

app = FastAPI()

app.include_router(userRoutes.userRouter)

app.include_router(compRoutes.compRouter)

app.include_router(entryRoutes.entryRouter)
