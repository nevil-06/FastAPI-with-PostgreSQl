from fastapi import FastAPI

from src.competition.router import competiton_router
from src.entry.router import entry_router
from src.user.router import user_router

app = FastAPI()


app.include_router(user_router)
app.include_router(entry_router)
app.include_router(competiton_router)


@app.get("/")
def display_start():
    return {"message": "database crud"}
