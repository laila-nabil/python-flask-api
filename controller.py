from db import get_db


def insert_test_case(title, steps , expected_result , actual_result, test_assets, status):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO test_cases(title, steps , expected_result , actual_result , test_assets , status) VALUES (?, ? , ?, ? , ?, ? )"
    cursor.execute(statement, [title, steps , expected_result , actual_result , test_assets, status])
    db.commit()
    return True


def update_test_case(id, title, steps , expected_result , actual_result, test_assets, status):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE test_cases SET title = ?, steps  = ? , expected_result  = ? , actual_result = ? , test_assets = ?, status = ? WHERE id = ?"
    cursor.execute(statement, [title, steps , expected_result , actual_result, test_assets, status ,id])
    db.commit()
    return True


def delete_test_case(id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM test_cases WHERE id = ?"
    cursor.execute(statement, [id])
    db.commit()
    return True


def get_by_id(id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT id, title, steps , expected_result , actual_result , test_assets , status FROM test_cases WHERE id = ?"
    cursor.execute(statement, [id])
    return cursor.fetchone()


def get_test_Cases():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id, title, steps , expected_result , actual_result , test_assets , status FROM test_cases"
    cursor.execute(query)
    return cursor.fetchall()