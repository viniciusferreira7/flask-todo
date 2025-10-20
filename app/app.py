from typing import List
from flask import Flask
from flasgger import Swagger

from routes.task_route import create_task

app = Flask(__name__)

swagger = Swagger(app)

tasks: List[dict] = []
task_id_control = 1

@app.route("/tasks", methods=["POST"])
def create_task_route():
    """
    Create a new task
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            title:
              type: string
              example: "Study Flask"
            description:
              type: string
              example: "Learn how to build APIs with Flask"
    responses:
      201:
        description: Task created successfully
    """
    global task_id_control
    
    return create_task(task_id_control, tasks)

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5001)