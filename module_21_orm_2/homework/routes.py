#!/usr/bin/env python3
if __name__ == '__main__':
    from flask import Flask, jsonify, request, render_template
    from sqlalchemy import func, extract
    from werkzeug.utils import secure_filename

    import datetime
    import os
    import csv

    from create_base import init_db
    from models import Book, ReceivingBooks, Student, session

    app = Flask(__name__)


    @app.route("/books/count/<int:id_author>", methods=["GET"])
    def count_books_by_author(id_author):
        """
        Gets количество оставшихся в библиотеке книг по автору
        """
        books = session.query(Book).filter_by(author_id=id_author).count()
        return jsonify(book_count=books), 200


    @app.route("/books/not-read/<int:id_student>", methods=["GET"])
    def books_not_read(id_student):
        """
        Gets список книг, которые студент не читал,
        при этом другие книги этого автора студент уже брал
        """
        student = session.query(Student).filter_by(id=id_student).one()
        not_read_books_obj = []
        for i in student.books:
            not_read_books_obj.append(session.query(Book.name, Book.author_id, Book.id).filter_by(
                author_id=i.author_id).filter(Book.name.isnot(i.name)).all())
        not_read_books = [
            {
                "book_name": tuple(book)[0][0],
                "author_id": tuple(book)[0][1],
                "book_id": tuple(book)[0][2],
            } for book in not_read_books_obj
        ]
        give_books = [i.to_json() for i in student.books]
        return jsonify(_not_read_books=not_read_books, give_books=give_books), 200


    @app.route("/books/current-month", methods=["GET"])
    def avg_give_books_current_month():
        """
        Gets среднее количество книг, которые студенты брали в этом месяце
        """
        avg_books = session.query(ReceivingBooks).filter(
            extract('month', ReceivingBooks.date_of_issue) == datetime.datetime.today().month
        ).count() / 2
        return jsonify(avg_books_current_month=avg_books), 200


    @app.route("/books/popular-book", methods=["GET"])
    def popular_book():
        """
        Gets самую популярную книгу среди студентов, у которых средний балл больше 4.0
        """
        book = session.query(Book.name, func.count(ReceivingBooks.book_id)).join(Book).join(Student).filter(
            Student.average_score > 4).group_by(
            ReceivingBooks.student_id).order_by(
            func.count(ReceivingBooks.book_id).desc()).first()
        popular_book = {
            "book_name": str(book[0]),
            "count_give": int(book[1]),
        }
        return jsonify(popular_book=popular_book), 200


    @app.route("/books/top-readers", methods=["GET"])
    def top_readers_by_year():
        """
        Gets ТОП-10 самых читающих студентов в этом году
        """
        student = session.query(Student.name, Student.surname, func.count(ReceivingBooks.book_id)).join(Student).filter(
            extract('year', ReceivingBooks.date_of_issue) == datetime.datetime.today().year).group_by(
            ReceivingBooks.student_id).order_by(
            func.count(ReceivingBooks.book_id).desc()).limit(10).all()
        top_readers = [
            {
                "name": tuple(reader)[0],
                "surname": tuple(reader)[1],
                "count_books": tuple(reader)[2],
            }
            for reader in student
        ]
        return jsonify(top_readers=top_readers), 200


    @app.route("/books/import/students", methods=['GET', 'POST'])
    def import_students():
        """
        Import csv-файл с данными по студентам,
        test_students.csv - текстовый файл для загрузки создается
        """
        if request.method == 'POST':
            file_obj = request.files['file']
            data_filename = secure_filename(file_obj.filename)
            filename = os.path.normpath(
                os.path.join(app.config['UPLOAD_FOLDER'], data_filename)
            )
            file_obj.save(filename)
            with open(filename, "r") as file:
                reader = csv.DictReader(file, delimiter=";")
                refund_book = []
                for i in reader:
                    i["scholarship"] = bool(i["scholarship"])
                    refund_book.append(i)
                session.bulk_insert_mappings(Student, refund_book)
                session.commit()
                print("success!!!")
            return render_template("index_2.html")
        return render_template("index.html")


    init_db()
    app.config['JSON_AS_ASCII'] = False
    UPLOAD_FOLDER = os.path.normpath(os.path.join(os.getcwd(), 'staticFiles'))
    ALLOWED_EXTENSIONS = {'csv'}
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.run()
