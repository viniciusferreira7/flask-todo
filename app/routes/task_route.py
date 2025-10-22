from typing import TypedDict, List
from flask import request, jsonify
from schemas.task import Task

from models.task import Tasks


class CreateTaskPayload(TypedDict):
    title: str
    description: str

def create_task(task_id_control: int, tasks: List[Tasks]):
    data: CreateTaskPayload = request.get_json()
    
    new_task = Tasks({ 
                      "id": task_id_control, 
                      "title": data.get("title"), 
                      "description": data.get("description") ,
                      "is_completed": False
                    })
    
    tasks.append(new_task)
    
    return jsonify({"message": "New task created successfully"})

def get_tasks(tasks: List[Tasks]):
    tasks_List: List[dict]  = [task.to_dict() for task in tasks]
    return jsonify({ "tasks": tasks_List, "total_tasks": len(tasks) })

def get_task(id: int, tasks: List[Tasks]):
    task: Task | None
    
    for item in tasks:
        if item.id == id:
            task = item
            return jsonify({ "task": task.to_dict() })
                
    return jsonify({"message": "Task not found"}), 404   
