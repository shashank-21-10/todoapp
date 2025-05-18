from fastapi import FastAPI
from .routes.todoroute import todoRouter
from fastapi.responses import FileResponse

app = FastAPI()

favicon_path = './src/favicon.ico'

@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)

app.include_router(todoRouter)

