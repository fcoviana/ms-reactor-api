from fastapi import FastAPI
from app.api.task import router as task_router

app = FastAPI()

app.include_router(task_router, prefix="/tasks", tags=["tasks"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Task Management API"}