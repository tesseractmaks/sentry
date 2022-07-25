import sqlite3

from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import  StringField
from wtforms.validators import InputRequired

from models import init_db, get_all_books, DATA


app = Flask(__name__)


class BookForm(FlaskForm):
    book_title = StringField(validators=[InputRequired()], label=('Book title'))
    author_name = StringField(validators=[InputRequired()], label=('Author full name'))


@app.route('/books')
def all_books():
    return render_template(
        'index.html',
        books=get_all_books(),
    )


@app.route('/books/add', methods=["GET", "POST"])
def add_books():
    form = BookForm()
    return render_template('add_book.html', form=form)


@app.route('/books/add_done', methods=["GET", "POST"])
def get_add_done():
    insert_data = """
                INSERT INTO 'table_books' (title, author) VALUES (?, ?);
            """
    form = BookForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            book_title, author_name = form.book_title.data, form.author_name.data
            with sqlite3.connect("table_books.db") as conn:
                cursor = conn.cursor()
                cursor.execute(insert_data, (book_title, author_name,))
    book = request.form.get("book_title")
    return render_template('add_done.html', form=form, book=book)


@app.route('/books/search', methods=["GET", "POST"])
def get_books():
    form = BookForm()
    books = get_all_books()
    return render_template('get_book.html', form=form, books=books)


@app.route('/books/author', methods=["GET", "POST"])
def get_result_search_books():
    author_name = request.form.get("author_name")
    get_data = """
               SELECT * FROM table_books WHERE author = ?;
           """
    count_views = """
    UPDATE table_books SET count_views = count_views + 1 WHERE author = ?;
    """
    with sqlite3.connect("table_books.db") as conn:
        cursor = conn.cursor()
        cursor.execute(get_data, (str(author_name), ))
        data_sql = cursor.fetchone()
        cursor.execute(count_views, (str(author_name),))
        data = dict(zip(("id", "title", "author", "count_views"), data_sql))
    return render_template('search_result_book.html', data=data)


if __name__ == '__main__':
    init_db(DATA)
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)

