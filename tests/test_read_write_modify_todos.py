import sqlite3
from datetime import date

import commands as commands
import model
from database import connect_db
from read_modify_write_todos import read_write_modify_todo_entry, read_todo_entry, write_todo_entry


def test_read_todo_entry_found():
    db = seeded_db()
    todo1 = read_todo_entry(db, 1)
    assert todo1.title == "Aufgabe 1"
    assert todo1.description == "Beschreibung 1"
    assert todo1.done is False
    assert todo1.due_on == date(2024, 1, 1)


def test_read_todo_entry_not_found():
    db = seeded_db()
    todo1 = read_todo_entry(db, 10)
    assert todo1 is None


def test_insert_todo_entry():
    db = connect_db()
    todo = model.ToDoEntry(
        id=10,
        title="Aufgabe 10",
        description="Beschreibung 10",
        done=False,
        due_on=date(2024, 1, 10)
    )
    write_todo_entry(db, todo)
    cursor = db.execute("SELECT count(*) FROM todo WHERE id = ?", (10,))
    assert cursor.fetchone()[0] == 1


def test_update_todo_entry():
    db = seeded_db()
    todo = model.ToDoEntry(
        id=2,
        title="Aktualisierte Aufgabe",
        description="Neue Beschreibung",
        done=False,
        due_on=date(2024, 1, 20)
    )
    write_todo_entry(db, todo)
    cursor = db.execute("SELECT count(*) FROM todo WHERE id = ?", (2,))
    assert cursor.fetchone()[0] == 1
    cursor = db.execute("SELECT * FROM todo WHERE id = ?", (2,))
    assert cursor.fetchone()["title"] == "Aktualisierte Aufgabe"


def test_set_done_to_true():
    db = seeded_db()
    todo1 = fetch_modified_todo_entry(db, todo_id=4, cmd=commands.SetDoneCommand(done_status=True))
    assert todo1.done is True

    todo2 = fetch_modified_todo_entry(db, todo_id=8, cmd=commands.SetDoneCommand(done_status=True))
    assert todo2.done is True


def test_set_done_to_false():
    db = seeded_db()
    todo1 = fetch_modified_todo_entry(db, todo_id=4, cmd=commands.SetDoneCommand(done_status=False))
    assert todo1.done is False

    todo2 = fetch_modified_todo_entry(db, todo_id=8, cmd=commands.SetDoneCommand(done_status=False))
    assert todo2.done is False


def test_set_due_date():
    db = seeded_db()
    todo1 = fetch_modified_todo_entry(db, todo_id=2, cmd=commands.SetDueDateCommand(due_date=date(2024, 1, 2)))
    assert todo1.due_on == date(2024, 1, 2)

    todo2 = fetch_modified_todo_entry(db, todo_id=5, cmd=commands.SetDueDateCommand(due_date=date(2024, 1, 2)))
    assert todo2.due_on == date(2024, 1, 2)


def test_cannot_change_due_date_after_already_done():
    db = seeded_db()
    todo1 = read_todo_entry(db, 8)
    assert todo1.done is True

    todo1 = fetch_modified_todo_entry(db, todo_id=8, cmd=commands.SetDueDateCommand(due_date=date(2024, 1, 2)))
    assert todo1.due_on == date(2024, 1, 8)


# Helper function
def fetch_modified_todo_entry(db: sqlite3.Connection, todo_id: int,
                              cmd: commands.ToDoCommand) -> model.ToDoEntry | None:
    read_write_modify_todo_entry(db, todo_id, cmd)
    return read_todo_entry(db, todo_id)


# Setup function
def seeded_db() -> sqlite3.Connection:
    db = connect_db()

    for i in range(1, 9):
        done = i > 6
        due_on = date(2024, 1, i)
        db.execute(
            "INSERT INTO todo (id, title, description, done, due_on) VALUES (?, ?, ?, ?, ?)",
            (i, f"Aufgabe {i}", f"Beschreibung {i}", done, due_on.toordinal()),
        )

    return db
