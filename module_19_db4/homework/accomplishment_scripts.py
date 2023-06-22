import sqlite3


if __name__ == "__main__":
    for i in range(1, 7):
        with open(f'hw_{i}/1_{i}.sql', 'r') as sql_file:
            sql_script: str = sql_file.read()

        with sqlite3.connect('homework.db') as conn:
            cursor: sqlite3.Cursor = conn.cursor()
            cursor.execute(sql_script)
            result = cursor.fetchall()
            print(f"Task: 1_{i}", '\n', result, '\n' * 2, '===========')



