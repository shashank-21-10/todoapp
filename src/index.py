from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .routes.todoroute import todoRouter

app = FastAPI()
app.mount("/static", StaticFiles(directory="./src/static"), name="static")



app.include_router(todoRouter)

