import sqlite3

if __name__ == "__main__":
    with sqlite3.connect("hw_3_database.db") as conn:
        cursor = conn.cursor()
        for i in range(1, 4):
            cursor.execute(f"SELECT count(*) FROM table_{i}")
            result = cursor.fetchall()
            print(f'table_{i} - {int(*list(*result))} records')
        cursor.execute(f"SELECT count(DISTINCT value) FROM table_1")
        result_2 = cursor.fetchall()
        print(f'table_1 unique records - {int(*list(*result_2))}')

        cursor.execute(f"select count(value) from table_1 where value in (select value from table_2)")
        result_3 = cursor.fetchall()
        print(f'table_1 unique records in table_2 - {int(*list(*result_3))}')

        cursor.execute(
            f"select count(value) "
            f"from table_1 where value in (select value from table_2) "
            f"and value in (select value from table_3);")
        result_4 = cursor.fetchall()
        print(f'table_1 unique records in table_2 and table_3 - {int(*list(*result_4))}')







