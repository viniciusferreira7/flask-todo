from typing import TypedDict,Dict, List, Any

from flask import Flask, request
from models.task import Tasks
from schemas.task import Task

app = Flask(__name__)

tasks: List[Task] = []

class CreateTaskPayload(TypedDict):
    title: str
    description: str

@app.route("/tasks", methods=["POST"])
def create_task():
    data: CreateTaskPayload = request.get_json()
    
    print(data)
    
    return 'Created'

if __name__ == "__main__":
    app.run(debug=True, host='localhost')

