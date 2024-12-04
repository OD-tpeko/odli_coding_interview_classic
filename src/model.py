from datetime import date
from dataclasses import dataclass


@dataclass
class ToDoEntry:
    id: int
    title: str
    description: str

    done: bool
    due_on: date
