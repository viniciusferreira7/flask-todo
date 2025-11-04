from typing import List
from app.schemas.task import Task

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