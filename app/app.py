from typing import List
from flask import Flask

from routes.task_route import create_task

app = Flask(__name__)

tasks: List[dict] = []
task_id_control = 1

@app.route("/tasks", methods=["POST"])
def create_task_route():
    global task_id_control
    
    return create_task(task_id_control, tasks)

if __name__ == "__main__":
    app.run(debug=True, host="localhost")