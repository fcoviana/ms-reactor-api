# app/schemas/task.py
from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    description: str

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str