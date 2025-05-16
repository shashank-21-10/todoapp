from pydantic import BaseModel, Field
from typing import Optional
class Todo(BaseModel):
    title:str
    description:str
    completed:bool = Field(default=False)


class UpdateTodo(BaseModel):
    title:Optional[str] = None
    description:Optional[str] = None
    completed:Optional[bool] = None

