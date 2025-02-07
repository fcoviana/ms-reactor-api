from app.models.task import Task

class MemoryRepository:
    def __init__(self):
        self.tasks = {}
        self.counter = 1

    def create(self, task: Task) -> Task:
        task.id = self.counter
        self.tasks[self.counter] = task
        self.counter += 1
        return task

    def list(self) -> list[Task]:
        return list(self.tasks.values())

    def delete(self, task_id: int) -> bool:
        if task_id in self.tasks:
            del self.tasks[task_id]
            return True
        return False