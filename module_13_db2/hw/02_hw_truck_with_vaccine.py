"""
Пожалуйста, запустите скрипт generate_hw_database.py прежде, чем приступать к выполнению практической работы.
После выполнения скрипта у вас должен появиться файл базы hw.db и в нем таблица table_truck_with_vaccine
Грузовик перевозит очень важную вакцину.

Условия хранения этой вакцины весьма необычные -- в отсеке должна быть температура  -18±2 градуса.
    Если температурный режим был нарушен - вакцина считается испорченной.

Для проверки состояния вакцины применяется датчик, который раз в час измеряет температуру внутри контейнера.
    Если в контейнере было хотя бы 3 часа с температурой, которая находится вне указанного выше диапазона -
    температурный режим считается нарушенным.

Пожалуйста, реализуйте функцию `check_if_vaccine_has_spoiled`,
    которая по номеру грузовика определяет, не испортилась ли вакцина.
"""
import sqlite3
# Тут считаю сколько раз была температура вне диапазона -18±2
sql_request = """
SELECT COUNT(*) FROM table_truck_with_vaccine WHERE truck_number = ? AND NOT temperature_in_celsius BETWEEN -18 AND 2
"""

sql_request_truck_number = """
SELECT truck_number FROM table_truck_with_vaccine 
"""


def get_truck_number(c: sqlite3.Cursor):
    c.execute(sql_request_truck_number)
    all_records = c.fetchall()
    return all_records


def check_if_vaccine_has_spoiled(
        c: sqlite3.Cursor,
        truck_number: str,
) -> bool:
        c.execute(sql_request, (truck_number, ))
        records, *_ = c.fetchall()
        return int(*records) >= 3


if __name__ == "__main__":
    vaccine_ruined = []
    vaccine_fresh = []
    with sqlite3.connect("hw.db") as conn:
        cursor = conn.cursor()
        all_records = get_truck_number(cursor)
        for number in all_records:
            if check_if_vaccine_has_spoiled(cursor, str(*number)):
                vaccine_ruined.append(1)
                print(f"вакцина испортилась - номер машины: {str(*number)}")
            else:
                vaccine_fresh.append(1)
                print(f"вакцина НЕ испортилась- номер машины: {str(*number)}")
    print("\nИспорченных вакцин:", len(vaccine_ruined), "\nДействующих вакцин:", len(vaccine_fresh))
