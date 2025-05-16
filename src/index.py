from fastapi import FastAPI
from .routes.todoroute import todoRouter
app = FastAPI()

app.include_router(todoRouter)

