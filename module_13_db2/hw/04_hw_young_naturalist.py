"""
Юный натуралист Петя решил посетить Юнтоловский заказник на рассвете и записать журнал всех птиц,
    которых он увидел в заказнике. Он написал программу, но, в процессе написания,
    так устал, что уснул на клавиатуре, отчего пол-программы стёрлось.

Наш юный натуралист точно помнит, что программа позволяла добавить в БД новую птицу и говорила ему,
    видел ли он такую птицу раньше.

Помогите восстановить исходный код программы ЮНат v0.1 ,
    реализовав функции log_bird (добавление новой птицы в БД) и check_if_such_bird_already_seen
    (проверка что мы уже видели такую птицу)

Пожалуйста помогите ему, реализовав функцию log_bird .
    При реализации не забудьте про параметризацию SQL запроса!
"""

import datetime
import sqlite3

generate_hw4_sql = """
CREATE TABLE "log_bird" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "bird_name"	VARCHAR(255) NOT NULL UNIQUE,
    "count"	INTEGER ,
    "date_time"	VARCHAR(100) NOT NULL
);
"""

check_bird_request = """
    SELECT * FROM log_bird WHERE bird_name = ?
"""

insert_bird_request = """
    INSERT INTO 'log_bird' (bird_name, date_time, count) VALUES (?, ?, ?);
"""


def generate_table():
    with sqlite3.connect("hw.db") as connection:
        c: sqlite3.Connection
        cursor = connection.cursor()
        cursor.executescript(generate_hw4_sql)
        c.commit()


def log_bird(
        c: sqlite3.Cursor,
        bird_name: str,
        date_time: str,
        count: int,
) -> None:
    c.execute(insert_bird_request, (bird_name, date_time,  count))
    print(f"Птица:{bird_name} записана в базу!")


def check_if_such_bird_already_seen(c: sqlite3.Cursor, bird_name: str) -> bool:
    check_bird = c.execute(check_bird_request, (bird_name,))
    return check_bird.fetchone()


if __name__ == "__main__":
    try:
        generate_table()
    except sqlite3.OperationalError:
        print("Таблица уже существует можно продолжать\n")
    print("Программа помощи ЮНатам v0.1")
    name = input("Пожалуйста введите имя птицы\n> ")
    count_str = input("Сколько птиц вы увидели?\n> ")
    count = int(count_str)
    right_now = datetime.datetime.utcnow().isoformat()

    with sqlite3.connect("hw.db") as connection:
        cursor = connection.cursor()
        if check_if_such_bird_already_seen(cursor, name):
            print("Такую птицу мы уже наблюдали!")
        else:
            log_bird(cursor, name, right_now, count)




