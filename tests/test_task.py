import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_task():
    response = client.post("/tasks/", json={"title": "Test Task", "description": "Test Description"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Task"
    assert data["description"] == "Test Description"
    assert "id" in data

def test_list_tasks():
    # Create tasks before listing
    client.post("/tasks/", json={"title": "Test Task 1", "description": "Test Description 1"})
    client.post("/tasks/", json={"title": "Test Task 2", "description": "Test Description 2"})
    
    response = client.get("/tasks/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["title"] == "Test Task 1"
    assert data[1]["title"] == "Test Task 2"

def test_delete_task():
    # Create a task before deleting
    response = client.post("/tasks/", json={"title": "Test Task", "description": "Test Description"})
    task_id = response.json()["id"]
    
    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Task deleted successfully"
    
    response = client.get("/tasks/")
    data = response.json()
    assert len(data) == 0