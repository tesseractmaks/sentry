import sqlite3

with open('task_1_create_schema.sql', 'r') as sql_file:
    sql_script: str = sql_file.read()


with sqlite3.connect('task_1_surrogate.db') as conn:
    cursor: sqlite3.Cursor = conn.cursor()
    cursor.executescript(sql_script)
    conn.commit()
