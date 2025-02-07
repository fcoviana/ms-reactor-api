from fastapi import Depends
from app.repositories.memory import MemoryRepository
from app.services.task_service import TaskService

memory_repository = MemoryRepository()

def get_task_repository() -> MemoryRepository:
    return memory_repository

def get_task_service(repository: MemoryRepository = Depends(get_task_repository)) -> TaskService:
    return TaskService(repository)