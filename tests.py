from typing import List
from app.schemas.task import Task
from typing import Optional

import pytest
import requests

BASE_URL = 'http://localhost:5001'

tasks: List[str] = []

def test_create_task():
    task: Task = {
        "title": "New task",
        "description": "Task`s description",
    }
    
    response = requests.post(f"{BASE_URL}/tasks", json=task)

    assert response.status_code == 201
    
    assert "message" in response.json()
    assert "id" in response.json()
    
    tasks.append(response.json()['id'])
    
def create_task(title: Optional[str] = None, description: Optional[str] = None):
    task: Task = {
        "title": title or "New task",
        "description": description or "Task`s description",
    }

    response = requests.post(f"{BASE_URL}/tasks", json=task)
    
    tasks.append(response.json()['id'])
    
    return response

def test_get_tasks():
    create_task("Buy groceries", "Buy milk, eggs, and bread")
    create_task("Finish project", "Complete the API integration module")
    create_task("Workout", "Leg day at the gym")
    create_task("Read a book", "Continue reading 'Clean Architecture'")
    create_task()

    response = requests.get(f"{BASE_URL}/tasks")

    response_json = response.json()
    
    assert response.status_code == 200
    assert "tasks" in response_json
    assert "total_tasks" in response_json

def test_get_task():
    created_task_response = create_task("Buy groceries", "Buy milk, eggs, and bread")

    task_id = created_task_response.json()['id']
    
    response = requests.get(f"{BASE_URL}/tasks/{task_id}")

    response_json = response.json()
    
    assert response.status_code == 200
    assert "task" in response_json
    assert task_id == response_json["task"]["id"]

def test_update_task():
    created_task_response = create_task("Buy groceries", "Buy milk, eggs, and bread")

    task_id = created_task_response.json()['id']
    
    updated_task: Task = {
        "title": "Updated title",
        "description": "updated description",
        "is_completed": True
    }

    response = requests.patch(f"{BASE_URL}/tasks/{task_id}", json=updated_task)

    assert response.status_code == 204
    
def test_delete_task():
    createdTaskResponse = create_task()
    
    task_id: str = createdTaskResponse.json()["id"] 
    
    response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
    
    tasks.remove(task_id)
    
    assert response.status_code == 204
    
    