import sqlite3

from database import seeded_db


def playground(db: sqlite3.Connection):
    # Your playground for testing
    pass


if __name__ == "__main__":
    db = seeded_db()
    playground(db)
    db.close()
