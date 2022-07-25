import sqlite3
from typing import List


DATA = [
    {'id': 0, 'title': 'A Byte of Python', 'author': 'Swaroop C. H.', 'count_views': 0},
    {'id': 1, 'title': 'Moby-Dick; or, The Whale', 'author': 'Herman Melville', 'count_views': 0},
    {'id': 3, 'title': 'War and Peace', 'author': 'Leo Tolstoy', 'count_views': 0},
]


class Book:
    def __init__(self, id: int, title: str, author: str, count_views: int):
        self.id = id
        self.title = title
        self.author = author
        self.count_views = count_views

    def __getitem__(self, item):
        return getattr(self, item)


def init_db(initial_records: List[dict]):
    with sqlite3.connect('table_books.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT name FROM sqlite_master "
            "WHERE type='table' AND name='table_books';"
        )
        exists = cursor.fetchone()
        # now in `exist` we have tuple with table name if table really exists in DB
        if not exists:
            cursor.executescript(
                'CREATE TABLE `table_books`'
                '(id INTEGER PRIMARY KEY AUTOINCREMENT, title, author, count_views INTEGER DEFAULT 0)'
            )
            cursor.executemany(
                """INSERT INTO table_books (title, author, count_views) VALUES (?, ?, ?);""",
                [(item['title'], item['author'], item['count_views']) for item in initial_records]
            )


def get_all_books() -> List[Book]:
    with sqlite3.connect('table_books.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * from `table_books`')
        all_books = cursor.fetchall()
        return [Book(*row) for row in all_books]
