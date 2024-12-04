import sqlite3


def connect_db() -> sqlite3.Connection:
    db = sqlite3.connect(":memory:")
    db.row_factory = sqlite3.Row
    with open("sql/schema.sql", "r") as f:
        db.executescript(f.read())
    return db
