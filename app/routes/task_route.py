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


class UpdateTaskPayload(TypedDict):
    title: str
    description: str
    is_completed: bool

def update_task(id: int, tasks: List[Tasks]):
    data: UpdateTaskPayload = request.get_json()
    
    for item in tasks:
        if item.id == id:
            item.title = data.get("title")
            item.description = data.get("description")
            item.is_completed = bool(data.get("is_completed"))
            
            return jsonify(), 204
                
    return jsonify({"message": "Task not found"}), 404   

def delete_task(id: int, tasks: List[Tasks]):
    task: Task | None = None
    
    for item in tasks:
        if item.id == id:
            task = item
            break
    
    if not task:
        return jsonify({ "message": "Not found" }), 404

    tasks.remove(task)
    
    return jsonify() ,204
        
    
    