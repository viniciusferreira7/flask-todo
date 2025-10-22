from schemas.task import Task

class Tasks:
    def __init__(self, task: Task):
        self.id = task.get("id")
        self.title = task.get("title")
        self.description = task.get("description")
        self.is_completed = task.get("is_completed")
        
    def to_dict(self) -> Task:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "is_completed": self.is_completed,
        }