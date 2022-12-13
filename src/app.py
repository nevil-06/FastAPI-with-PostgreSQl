from fastapi import FastAPI
from .user.router import user_router
from .entry.router import entry_router 
from .competition.router import competiton_router


app = FastAPI()


app.include_router(user_router)
app.include_router(entry_router)
app.include_router(competiton_router)


@app.get('/')
def display_start():
    return {"message : database crud"}
