"""
Вы работаете программистом в IT отделе ГИБДД.
    Ваш отдел отвечает за обслуживание камер,
    которые фиксируют превышения скорости и выписывают автоматические штрафы.
За последний месяц к вам пришло больше тысячи жалоб на ошибочно назначенные штрафы,
    из которых около 100 были признаны и правда ошибочными.

Список из дат и номеров автомобилей ошибочных штрафов прилагается к заданию,
    пожалуйста удалите записи об этих штрафах из таблицы `table_fees`
"""
import sqlite3
import csv

delete_request = """
DELETE FROM table_fees WHERE truck_number = ? AND timestamp = ?
"""


def delete_wrong_fees(c: sqlite3.Cursor, wrong_fees_file: str) -> None:
    with open(wrong_fees_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=",")
        for line in reader:
            c.execute(delete_request, (line['car_number'], line['timestamp']))


if __name__ == "__main__":
    with sqlite3.connect("hw.db") as conn:
        cursor = conn.cursor()
        delete_wrong_fees(cursor, "wrong_fees.csv")
