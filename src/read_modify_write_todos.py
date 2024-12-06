import sqlite3
from datetime import date

import model


# Function to read a ToDoEntry from the database using its ID, or None if not found
def read_todo_entry(db: sqlite3.Connection, todo_id: int) -> model.ToDoEntry | None:
    # Implement database fetching here
    pass


# Function to apply the given due date to a ToDoEntry, respecting business rules
def apply_due_on(todo: model.ToDoEntry, due_on: date) -> None:
    # Implement due date application here
    pass


# Function to save a ToDoEntry to the database
def write_todo_entry(db: sqlite3.Connection, todo: model.ToDoEntry) -> None:
    # Implement database saving here
    pass


# Function that combines the glues the above functions together
def read_write_modify_todo_entry(db: sqlite3.Connection, todo_id: int, due_on: date):
    # Fetch todo entry from database
    todo_entry = read_todo_entry(db, todo_id)
    # Abort if not found
    if todo_entry is None:
        return None

    # Apply change on todo entry
    apply_due_on(todo_entry, due_on)

    # Save todo entry back to database
    write_todo_entry(db, todo_entry)
