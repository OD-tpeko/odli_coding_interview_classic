from datetime import date

import pytest

import model
from database import seeded_db
from read_modify_write_todos import read_write_modify_todo_entry, read_todo_entry, write_todo_entry, apply_due_on


def test_read_todo_entry_found(db):
    todo1 = read_todo_entry(db, 2)
    assert todo1.title == "Sportplan aufstellen"
    assert todo1.description == "Mehr Fitnessstudio im neuen Jahr"
    assert todo1.done is False
    assert todo1.due_on == date(2025, 1, 1)


def test_read_todo_entry_not_found(db):
    todo1 = read_todo_entry(db, 10)
    assert todo1 is None


def test_insert_todo_entry(db):
    todo = model.ToDoEntry(
        id=10,
        title="Test vorbereiten",
        description="Gemeinsam im Team den Test durchgehen",
        done=False,
        due_on=date(2024, 12, 10)
    )
    write_todo_entry(db, todo)
    cursor = db.execute("SELECT count(*) FROM todo WHERE id = ?", (10,))
    assert cursor.fetchone()[0] == 1
    row = db.execute("SELECT * FROM todo WHERE id = ?", (10,)).fetchone()
    assert row["title"] == "Test vorbereiten"
    assert row["description"] == "Gemeinsam im Team den Test durchgehen"
    assert row["done"] == 0
    assert row["due_on"] == date(2024, 12, 10).toordinal()


def test_update_todo_entry(db):
    todo = model.ToDoEntry(
        id=2,
        title="Aktualisierte Aufgabe",
        description="Neue Beschreibung",
        done=True,
        due_on=date(2024, 1, 20)
    )
    write_todo_entry(db, todo)
    cursor = db.execute("SELECT count(*) FROM todo WHERE id = ?", (2,))
    assert cursor.fetchone()[0] == 1
    row = db.execute("SELECT * FROM todo WHERE id = ?", (2,)).fetchone()
    assert row["title"] == "Aktualisierte Aufgabe"
    assert row["description"] == "Neue Beschreibung"
    assert row["done"] == 1
    assert row["due_on"] == date(2024, 1, 20).toordinal()


def test_set_due_on_happy_path():
    todo = model.ToDoEntry(
        id=2,
        title="Dummy Aufgabe",
        description="Eine kleine süße Beschreibung",
        done=False,
        due_on=date(2024, 12, 16)
    )
    apply_due_on(todo, date(2025, 1, 1))
    assert todo.due_on == date(2025, 1, 1)


def test_set_due_on_raises_exception():
    todo = model.ToDoEntry(
        id=2,
        title="Erledigte Aufgabe",
        description="Eine kleine süße Beschreibung",
        done=True,
        due_on=date(2024, 12, 16)
    )
    with pytest.raises(Exception):
        apply_due_on(todo, date(2025, 1, 1))
    assert todo.due_on == date(2024, 12, 16)


def test_set_due_on_silent_if_no_change():
    todo = model.ToDoEntry(
        id=2,
        title="Erledigte Aufgabe",
        description="Eine kleine süße Beschreibung",
        done=True,
        due_on=date(2024, 12, 16)
    )
    apply_due_on(todo, date(2024, 12, 16))
    assert todo.due_on == date(2024, 12, 16)


def test_pipeline_happy_path(db):
    read_write_modify_todo_entry(db, 2, due_on=date(2025, 2, 1))
    row = db.execute("SELECT * FROM todo WHERE id = ?", (2,)).fetchone()
    assert row["due_on"] == date(2025, 2, 1).toordinal()


def test_pipeline_raises_exception(db):
    with pytest.raises(Exception):
        read_write_modify_todo_entry(db, 4, due_on=date(2025, 2, 1))
    row = db.execute("SELECT * FROM todo WHERE id = ?", (4,)).fetchone()
    assert row["due_on"] == date(2024, 11, 21).toordinal()


@pytest.fixture
def db():
    db = seeded_db()
    yield db
    db.close()
