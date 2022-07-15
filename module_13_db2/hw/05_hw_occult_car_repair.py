"""
В 20NN году оккультному автосалону "Чёртово колесо" исполняется ровно 13 лет.
    В честь этого они предлагает своим клиентам уникальную акцию:
    если вы обращаетесь в автосалон в пятницу тринадцатое и ваш автомобиль
    чёрного цвета и марки "Лада" или "BMW", то вы можете поменять колёса со скидкой 13%.
Младший менеджер "Чёртова колеса" слил данные клиентов в интернет,
    поэтому мы можем посчитать, как много клиентов автосалона могли воспользоваться
    скидкой (если бы они об этом знали). Давайте сделаем это!

Реализуйте функцию, c именем get_number_of_luckers которая принимает на вход курсор и номер месяца,
    и в ответ возвращает число клиентов, которые могли бы воспользоваться скидкой автосалона.
    Таблица с данными называется `table_occult_car_repair`
"""
import sqlite3

sql_request = """
SELECT COUNT(*) FROM table_occult_car_repair WHERE (strftime('%m', timestamp)=? AND car_colour = 'чёрный') AND (car_type='Лада' OR car_type='BMW')
"""


def get_number_of_luckers(
        c: sqlite3.Cursor, month_number: str,
):
    c.execute(sql_request, (month_number, ))
    number_of_luckers, *_ = c.fetchall()
    print("Число счастливых клиентов:", int(*number_of_luckers))


if __name__ == "__main__":
    month_number = input("Введите номер месяца: ")
    while True:
        if 1 <= int(month_number) <= 12:
            break
        print("Введите номер месяца в диапазоне 1-12")
        month_number = input("Введите номер месяца: ")

    with sqlite3.connect("hw.db") as conn:
        cursor = conn.cursor()
        if 1 <= int(month_number) < 10:
            month_number = f"0{month_number}"
        get_number_of_luckers(cursor, month_number)

