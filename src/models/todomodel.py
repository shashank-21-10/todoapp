from pydantic import BaseModel
from typing import Optional
class Todo(BaseModel):
    title:str
    description:str


class UpdateTodo(BaseModel):
    title:Optional[str] = None
    description:Optional[str] = None

