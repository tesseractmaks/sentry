import sqlite3
from typing import List, Dict

from flask import Flask, render_template, request

from models import init_db, get_all_books, DATA


app = Flask(__name__)


def _get_html_table_for_books(books: List[Dict]) -> str:
    table = """
<table>
    <thead>
    <tr>
        <th>ID</td>
        <th>Title</td>
        <th>Author</td>
    </tr>
    </thead>
    <tbody>
        {books_rows}
    </tbody>
</table>
"""
    rows = ''
    for book in books:
        rows += '<tr><td>{id}</tb><td>{title}</tb><td>{author}</tb></tr>'.format(
            id=book['id'], title=book['title'], author=book['author'],
        )
    return table.format(books_rows=rows)


@app.route('/books')
def all_books():
    return render_template(
        'index.html',
        books=get_all_books(),
    )


@app.route('/books/form')
def get_books_form():
    return render_template('add_book.html')


@app.route('/books/add', methods=["POST"])
def get_books():
    insert_data = """
        INSERT INTO 'table_books' (title, author) VALUES (?, ?);
    """

    book_title = request.form.get('field1')
    author_name = request.form.get('field2')

    with sqlite3.connect("table_books.db") as conn:
        cursor = conn.cursor()
        cursor.execute(insert_data, (book_title, author_name, ))

    return render_template('add_book.html')


if __name__ == '__main__':
    init_db(DATA)
    app.run(debug=True)
