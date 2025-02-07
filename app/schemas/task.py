from typing import TypedDict

class Task(TypedDict):
    id: int
    title: str
    description: str
    is_completed: bool = False