import sqlite3
import random
import string
last_names = """
Иванов
Васильев
Петров
Смирнов
Соловьёв
""".split()

first_names = """
Иван
Василь
Петр
Смирд
Соловей
""".split()

middle_names = """
Иванович
Васильевич
Петрович
Смирнович
Соловьёвич
""".split()

book_names = """
Книга Иваныча,
Книга Василича,
Книга Петровича,
Книга Смирновича,
Книга Соловьёвича,
""".split(',')


def _get_random_book_names_author_id(book_names):
    book_name = random.choice(book_names)
    author_id = random.randint(1, 10)
    return book_name + "".join([random.choice(string.ascii_letters) for _ in range(1, 5)]), author_id


def _get_random_fio(last_names, first_names, middle_names):
    last_name = random.choice(last_names)
    first_name = random.choice(first_names)
    middle_name = random.choice(middle_names)
    return last_name, first_name, middle_name


if __name__ == "__main__":

    with open('schema_scripts.sql', 'r') as sql_file:
        sql_script: str = sql_file.read()

    with sqlite3.connect('books.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.executescript(sql_script)
        fio = [(_get_random_fio(last_names, first_names, middle_names)) for _ in range(1, 11)]
        book_names = [(_get_random_book_names_author_id(book_names)) for _ in range(1, 35)]
        cursor.executemany(
            "INSERT INTO 'author' (first_name, last_name, middle_name) values (?, ?, ?)",
            fio
        )
        cursor.executemany(
            "INSERT INTO 'books' (book_name, author) values (?, ?)",
            book_names
        )
        conn.commit()
