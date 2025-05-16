from fastapi import APIRouter
from ..schemas.todoschema import todoListSerializer, todoSerializer
from ..config.database import TodoCollection
from ..models.todomodel import Todo, UpdateTodo
from bson import ObjectId

todoRouter = APIRouter()

@todoRouter.get('/')
def getTodos():
    todos = todoListSerializer(TodoCollection.find())
    return {"todos":todos , "message":"Todos Fetched Successfully"}

@todoRouter.post('/')
async def createTodo(todo : Todo):
    existTodo = TodoCollection.insert_one(dict(todo))
    print(f"EXISTTODO : {existTodo}")
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
        "description": f"{todo.description if todo.description != None else existTodo["description"]}",
        "completed": f"{todo.completed if todo.completed != None else existTodo["completed"]}"
    })

    TodoCollection.update_one({"_id" : ObjectId(id)} , {"$set" : newTodo})
    return {"message":"Todo Updated Successfully"}