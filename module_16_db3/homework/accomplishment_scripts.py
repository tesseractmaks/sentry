import sqlite3


if __name__ == "__main__":
    # for i in range(3, 8):

    with open('2_7.sql', 'r') as sql_file:
        sql_script: str = sql_file.read()

    with sqlite3.connect('hw.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute(sql_script)
        result = cursor.fetchall()
        print("Task: 2_3", '\n', result, '\n' * 2, '===========')
        print("Task: 2_4", '\n', result, '\n' * 2, '===========')
        print("Task: 2_7", '\n', result, '\n' * 2, '===========')


