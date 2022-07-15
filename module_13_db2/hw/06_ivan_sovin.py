"""
Иван Совин - эффективный менеджер.
Когда к нему приходит сотрудник просить повышение з/п -
    Иван может повысить её только на 10%.

Если после повышения з/п сотрудника будет больше з/п самого
    Ивана Совина - сотрудника увольняют, в противном случае з/п
    сотрудника повышают.

Давайте поможем Ивану стать ещё эффективнее,
    автоматизировав его нелёгкий труд.
    Пожалуйста реализуйте функцию которая по имени сотрудника
    либо повышает ему з/п, либо увольняет сотрудника
    (удаляет запись о нём из БД).

Таблица с данными называется `table_effective_manager`
"""
import sqlite3

update_request = """
UPDATE table_effective_manager  SET salary = ? WHERE name=?
"""

delete_request = """
DELETE * FROM table_effective_manager WHERE name=?
"""

get_salary_request = """
SELECT salary FROM table_effective_manager WHERE name=? 
"""


def ivan_sovin_the_most_effective(
        c: sqlite3.Cursor,
        name: str,
) -> None:

    c.execute(get_salary_request, (name, ))
    salary, *_ = c.fetchone()
    if int(salary) > (IVAN_SALARY + (IVAN_SALARY * 0.1)):
        print(f'У {name} зарплата:{salary}')
        c.execute(delete_request, (name,))
        print(f'{name} уволен!')
    else:
        print(f'У {name} зарплата:{salary}')
        new_salary = salary + (salary * 0.1)
        c.execute(update_request, (new_salary, name, ))
        c.execute(get_salary_request, (name,))
        update_salary, *_ = c.fetchone()
        print(f'У {name} зарплата повышена на {salary * 0.1} до:{update_salary}')


#  Сотрудники для теста: Дмитриев Ш.Щ., Андреева В.Л., Васильева Щ.А.

if __name__ == "__main__":
    IVAN_SALARY = 100000
    with sqlite3.connect("hw.db") as conn:
        cursor = conn.cursor()
        name = input("Введите имя сотрудника: ")
        ivan_sovin_the_most_effective(cursor, name)

