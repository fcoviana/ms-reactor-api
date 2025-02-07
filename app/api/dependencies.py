from fastapi import Depends
from app.repositories.memory import MemoryRepository

def get_task_repository() -> MemoryRepository:
    return MemoryRepository()