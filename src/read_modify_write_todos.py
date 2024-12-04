import sqlite3
from datetime import date

import commands
import model


# Function to read a ToDoEntry from the database using its ID, or None if not found
def read_todo_entry(db: sqlite3.Connection, todo_id: int) -> model.ToDoEntry | None:
    # Implement database fetching here
    cursor = db.execute("SELECT * FROM todo WHERE id = ?", (todo_id,))
    row = cursor.fetchone()
    if row is None:
        return None
    return model.ToDoEntry(
        id=row["id"],
        title=row["title"],
        description=row["description"],
        done=bool(row["done"]),
        due_on=date.fromordinal(row["due_on"]),
    )


# Function to modify a ToDoEntry according the given command, respecting business rules
def apply_on_todo_entry(todo: model.ToDoEntry, cmd: commands.ToDoCommand) -> None:
    # Implement command application here
    if isinstance(cmd, commands.SetDoneCommand):
        todo.done = cmd.done_status
    if isinstance(cmd, commands.SetDueDateCommand):
        if todo.done:
            return
        todo.due_on = cmd.due_date


# Function to save a ToDoEntry to the database
def write_todo_entry(db: sqlite3.Connection, todo: model.ToDoEntry) -> None:
    # Implement database saving here
    db.execute("""
        INSERT INTO todo (id, title, description, done, due_on)
        VALUES (:id, :title, :description, :done, :due_on)
        ON CONFLICT(id) DO 
        UPDATE SET title = :title, description = :description, done = :done, due_on = :due_on;
    """, dict(
        id=todo.id,
        title=todo.title,
        description=todo.description,
        done=todo.done,
        due_on=todo.due_on.toordinal()
    ))


# Function that combines the glues the above functions together
def read_write_modify_todo_entry(db: sqlite3.Connection, todo_id: int, cmd: commands.ToDoCommand):
    # Fetch todo entry from database
    todo_entry = read_todo_entry(db, todo_id)
    # Abort if not found
    if todo_entry is None:
        return None

    # Apply change on todo entry
    apply_on_todo_entry(todo_entry, cmd)

    # Save todo entry back to database
    write_todo_entry(db, todo_entry)
