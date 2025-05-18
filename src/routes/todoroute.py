from fastapi import APIRouter, Request
from ..schemas.todoschema import todoListSerializer
from ..config.database import TodoCollection
from ..models.todomodel import Todo, UpdateTodo
from bson import ObjectId
from fastapi.templating import Jinja2Templates

todoRouter = APIRouter()

templates = Jinja2Templates(directory="./src/templates")

@todoRouter.get('/')
def getTodos(request: Request):
    todos = todoListSerializer(TodoCollection.find())

    return templates.TemplateResponse(
        request=request, name="index.html", context={"todos":todos , "message":"Working Fine"}
    )

@todoRouter.post('/')
async def createTodo(todo : Todo):
    TodoCollection.insert_one(dict(todo))
    return {"message": "Todo Created Successfully"}

@todoRouter.delete('/{id}')
async def deleteTodo(id : str):
    existTodo = TodoCollection.delete_one({"_id" : ObjectId(id)})
    print(f"EXISTTODO : {existTodo}")
    return {"message":"Todo Deleted Successfully"}

@todoRouter.put("/{id}")
async def updateTodo(id : str , todo:UpdateTodo):
    existTodo = TodoCollection.find_one({"_id" : ObjectId(id)})
    print(f"EXISTTODO : {existTodo}")
    newTodo = dict({
        "title": f"{todo.title if todo.title != None else existTodo["title"]}",
        "description": f"{todo.description if todo.description != None else existTodo["description"]}"
    })

    TodoCollection.update_one({"_id" : ObjectId(id)} , {"$set" : newTodo})
    return {"message":"Todo Updated Successfully"}