# app/api/task.py
from fastapi import APIRouter, HTTPException, Depends
from app.schemas.task import TaskCreate, TaskResponse
from app.services.task_service import TaskService
from app.repositories.memory import MemoryRepository

router = APIRouter()

def get_task_service():
    repository = MemoryRepository()
    return TaskService(repository)

task_service = get_task_service()

@router.post("/tasks/", response_model=TaskResponse)
async def create_task(task: TaskCreate, service: TaskService = Depends(get_task_service)):
    return service.create_task(task)

@router.get("/tasks/", response_model=list[TaskResponse])
async def list_tasks(service: TaskService = Depends(get_task_service)):
    return service.list_tasks()

@router.delete("/tasks/{task_id}", response_model=dict)
async def delete_task(task_id: int, service: TaskService = Depends(get_task_service)):
    success = service.delete_task(task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"}