from typing import List
from flask import Flask
from flasgger import Swagger

from routes.task_route import create_task, get_tasks

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
    
    print(task_id_control)
    
    response = create_task(task_id_control, tasks)
    
    task_id_control +=1

    return response
  
@app.route("/tasks", methods=["GET"])
def get_tasks_route():
    """
    Get all tasks
    ---
    responses:
      200:
        description: List of all tasks
        schema:
          type: object
          properties:
            tasks:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                    example: 1
                  title:
                    type: string
                    example: "Study Flask"
                  description:
                    type: string
                    example: "Learn how to build APIs with Flask"
                  is_completed:
                    type: boolean
                    example: false
            total_tasks:
              type: integer
              example: 5
    """
    return get_tasks(tasks)

  

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5001)