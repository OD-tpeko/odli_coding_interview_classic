import sqlite3

from database import connect_db


def playground(db: sqlite3.Connection):
    # Your playground for testing
    pass


if __name__ == "__main__":
    db = connect_db()
    playground(db)