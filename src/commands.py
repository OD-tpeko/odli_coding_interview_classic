import abc
from dataclasses import dataclass
from datetime import date


class ToDoCommand(abc.ABC):
    pass


@dataclass(frozen=True)
class SetDoneCommand(ToDoCommand):
    done_status: bool


@dataclass(frozen=True)
class SetDueDateCommand(ToDoCommand):
    due_date: date
