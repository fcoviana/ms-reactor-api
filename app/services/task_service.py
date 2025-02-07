from typing import List
from app.models.task import Task
from app.repositories.memory import MemoryRepository
from app.schemas.task import TaskCreate

class TaskService:
    def __init__(self, repository: MemoryRepository):
        self.repository = repository

    def create_task(self, task_data: TaskCreate) -> Task:
        task = Task(id=0, title=task_data.title, description=task_data.description)
        return self.repository.create(task)

    def list_tasks(self) -> List[Task]:
        return self.repository.list()

    def delete_task(self, task_id: int) -> bool:
        return self.repository.delete(task_id)