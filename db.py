import sqlite3
DATABASE_NAME = "test_cases.db"


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_tables():
    tables = [
               """CREATE TABLE IF NOT EXISTS test_cases(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                steps TEXT NOT NULL,
				expected_result TEXT NOT NULL,
				actual_result TEXT,
				test_assets TEXT,
				status INTEGER NOT NULL
            )
            """
    ]
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)