from dataclasses import dataclass
from typing import Optional
import sqlite3

BOOKS_TABLE_NAME = "books"
AUTHORS_TABLE_NAME = "author"
DATABASE_NAME = "books.db"


@dataclass
class Book:
    book_name: str
    author: Optional[int]
    book_id: Optional[int]

    def __getitem__(self, item):
        return getattr(self, item)


@dataclass
class Author:
    first_name: str
    last_name: str
    middle_name: str
    author_id: Optional[int]

    def __getitem__(self, item):
        return getattr(self, item)


def _get_book_obj_from_row(row):
    return Book(book_id=row[0], author=row[1], book_name=row[2])


def _get_author_obj_from_row(row):
    return Author(author_id=row[0], first_name=row[1], last_name=row[2], middle_name=row[3])


def get_all_obj(TABLE_NAME):
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute(
            f"SELECT * FROM `{TABLE_NAME}`"
        )
        all_obj = cursor.fetchall()
        if TABLE_NAME == "author":
            return [_get_author_obj_from_row(row) for row in all_obj]
        return [_get_book_obj_from_row(row) for row in all_obj]


def get_obj_by_id(TABLE_NAME, obj_names_column, obj_id: int):
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        names_column = None
        if "book_id" in obj_names_column:
            names_column = "book_id"
        if "author_id" in obj_names_column:
            names_column = "author_id"
        qry = f"SELECT * FROM `{TABLE_NAME}` WHERE {names_column} = '%s'" % obj_id
        cursor.execute(qry, )
        result = cursor.fetchone()
        if result and names_column == "author_id":
            return _get_author_obj_from_row(result)
        if result and names_column == "book_id":
            return _get_book_obj_from_row(result)


def add_obj(TABLE_NAME, obj_class):
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        qry_table = f"INSERT INTO `{TABLE_NAME}` "
        names_column = str(tuple(obj_class.keys())[:-1])
        values_column = tuple(obj_class.values())[:-1]
        param_values = f"{'?,' * len(values_column)}"[:-1]
        qry = f"{qry_table}{names_column} VALUES ({param_values})"
        cursor.execute(qry, values_column)
        obj_class[str(tuple(obj_class.keys())[-1])] = cursor.lastrowid
        return obj_class


def delete_obj_by_id(TABLE_NAME, obj_names_column, obj_id: int) -> None:
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        names_column = None
        if "book_id" in obj_names_column:
            names_column = "book_id"
        if "author_id" in obj_names_column:
            names_column = "author_id"
        qry = f"DELETE FROM `{TABLE_NAME}` WHERE {names_column} = '%s'" % obj_id
        cursor.execute(qry, )
        conn.commit()


def update_obj_by_id(TABLE_NAME, obj_class, obj_id):
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        names_column = tuple(obj_class.keys())[:-1]
        values_column = tuple(obj_class.values())[:-1]
        qry = f"UPDATE `{TABLE_NAME}` SET "
        for name, value in zip(names_column, values_column):
            qry += f"{name} = '{value}',"
        names_column = None
        if "book_id" in tuple(obj_class.keys()):
            names_column = "book_id"
        if "author_id" in tuple(obj_class.keys()):
            names_column = "author_id"
        qry = qry[:-1] + f"WHERE {names_column} = {obj_id}"
        cursor.execute(qry)
        conn.commit()


def update_patch_obj_by_id(TABLE_NAME, obj_class, obj_id):
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        names_column = tuple(obj_class.keys())
        values_column = tuple(obj_class.values())
        qry = f"UPDATE `{TABLE_NAME}` SET "
        for name, value in zip(names_column, values_column):
            qry += f"{name} = '{value}',"
        names_column = None
        if TABLE_NAME == "books":
            names_column = "book_id"
        if TABLE_NAME == "author":
            names_column = "author_id"
        qry = qry[:-1] + f"WHERE {names_column} = {obj_id}"
        cursor.execute(qry)
        conn.commit()


def get_book_by_title(TABLE_NAME, book_title: str) -> Optional[Book]:
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT * FROM `{TABLE_NAME}` WHERE book_name = ?
            """,
            (book_title,)
        )
        book = cursor.fetchone()
        if book:
            return _get_book_obj_from_row(book)
