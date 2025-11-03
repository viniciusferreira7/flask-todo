from typing import List
from flask import Flask
from flasgger import Swagger

from routes.task_route import create_task, get_tasks, get_task, update_task, delete_task

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

@app.route("/tasks/<int:id>", methods=["GET"])
def get_task_route(id: int):
  """
  Get a specific task by ID
  ---
  parameters:
    - name: id
      in: path
      type: integer
      required: true
      example: 1
  responses:
    200:
      description: Task retrieved successfully
      schema:
        type: object
        properties:
          task:
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
    404:
      description: Task not found
  """
  return get_task(id, tasks)
  
@app.route("/tasks/<int:id>", methods=["PATCH"])
def update_task_route(id: int):
  """
  Update a specific task by ID
  ---
  parameters:
    - name: id
      in: path
      type: integer
      required: true
      example: 1
    - name: body
      in: body
      required: true
      schema:
        type: object
        properties:
          title:
            type: string
            example: "Study Flask Advanced"
          description:
            type: string
            example: "Learn advanced Flask concepts and best practices"
          is_completed:
            type: boolean
            example: false
  responses:
    204:
      description: Task updated successfully
    404:
      description: Task not found
  """
  return update_task(id, tasks)

@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task_route(id: int):
  """
  Delete a specific task by ID
  ---
  parameters:
    - name: id
      in: path
      type: integer
      required: true
      example: 1
  responses:
    204:
      description: Task deleted successfully
    404:
      description: Task not found
  """
  return delete_task(id, tasks)

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5001)