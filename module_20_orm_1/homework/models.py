import os

from sqlalchemy.exc import NoResultFound

if __name__ == '__main__':
    import datetime
    import random
    from sqlalchemy import func, create_engine, Column, Integer, String, Date, Float, Boolean
    from sqlalchemy.orm import sessionmaker, declarative_base
    from sqlalchemy.ext.hybrid import hybrid_property
    from flask import Flask, jsonify, abort, request
    from create_base import book_names, \
        get_random_date, \
        last_names, \
        middle_names, \
        first_names, \
        generate_email, \
        generate_phone

    app = Flask(__name__)

    engine = create_engine("sqlite:///homework.db")
    Session = sessionmaker(bind=engine)
    session = Session()
    Base = declarative_base()


    class Books(Base):
        __tablename__ = "books"

        id = Column(Integer, primary_key=True)
        name = Column(String(50), nullable=False)
        count = Column(Integer, default=1)
        realese_date = Column(Date, nullable=False)
        author_id = Column(Integer, nullable=False)

        def __repr__(self):
            return '{} {} {} {} {}'.format(
                self.name,
                self.count,
                self.realese_date,
                self.id,
                self.author_id
            )

        def to_json(self):
            return {c.name: getattr(self, c.name) for c in self.__table__.columns}

        @classmethod
        def get_book_by_name(cls, name: str):
            try:
                book = session.query(Books).filter(Books.name.contains(name)).all()
                return book
            except Exception:
                pass


    class Authors(Base):
        __tablename__ = "authors"

        id = Column(Integer, primary_key=True)
        name = Column(String(50), nullable=False)
        surname = Column(String(50), nullable=False)

        def __repr__(self):
            return '{} {} {}'.format(
                self.id,
                self.surname,
                self.name,
            )

        def to_json(self):
            return {c.name: getattr(self, c.name) for c in self.__table__.columns}


    class Students(Base):
        __tablename__ = "students"

        id = Column(Integer, primary_key=True)
        name = Column(String(50), nullable=False)
        surname = Column(String(50), nullable=False)
        phone = Column(String(10), nullable=False)
        email = Column(String(50), nullable=False)
        average_score = Column(Float, nullable=False)
        scholarship = Column(Boolean, nullable=False)

        def __repr__(self):
            return '{} {} {} {} {} {} {}'.format(
                self.scholarship,
                self.average_score,
                self.id,
                self.email,
                self.phone,
                self.surname,
                self.name,
            )

        def to_json(self):
            return {c.name: getattr(self, c.name) for c in self.__table__.columns}

        @classmethod
        def get_stutents_scholarship(cls):
            return session.query(Students).filter(Students.scholarship == True).all()

        @classmethod
        def get_average_score_higher(cls, avg_score):
            return session.query(Students).filter(Students.average_score > avg_score).all()


    class ReceivingBooks(Base):
        __tablename__ = "receiving_books"

        id = Column(Integer, primary_key=True)
        book_id = Column(Integer, nullable=False)
        student_id = Column(Integer, nullable=False)
        date_of_issue = Column(Date, nullable=False)
        date_of_return = Column(Date)

        def __repr__(self):
            return '{} {} {} {} {}'.format(
                self.date_of_issue,
                self.date_of_return,
                self.id,
                self.student_id,
                self.book_id,
            )

        def to_json(self):
            return {c.name: getattr(self, c.name) for c in self.__table__.columns}

        @hybrid_property
        def count_date_with_book(self):
            days = session.query(
                func.julianday(datetime.date.today()) - func.julianday(self.date_of_issue)).one()
            if not self.date_of_return and int(days[0]) > 14:
                return "Poganec!", int(*days)

            return "Good boy", int(*days)


    @app.route("/books", methods=["GET"])
    def all_boks():
        books = session.query(Books).all()
        books_list = []
        for book in books:
            books_list.append(book.to_json())
        return jsonify(books_list=books_list), 200


    @app.route("/debtors", methods=["GET"])
    def all_debtor():
        # days = session.query(func.julianday(datetime.date.today()) - func.julianday(ReceivingBooks.date_of_issue)).all()
        debtors = session.query(ReceivingBooks).filter(func.julianday(
            func.julianday(ReceivingBooks.date_of_issue) - func.julianday(ReceivingBooks.date_of_return)) > 14).all()
        debtors_list = []
        for debtor in debtors:
            debtors_list.append(debtor.to_json())
        return jsonify(debtors_list=debtors_list), 200


    @app.route("/give-book", methods=["POST"])
    def give_book_to_student():
        book_id = request.form.get("book_id", type=int)
        student_id = request.form.get("student_id", type=int)
        date_of_issue = datetime.date.today()
        add_book = ReceivingBooks(
            book_id=book_id,
            student_id=student_id,
            date_of_issue=date_of_issue,
        )
        session.add(add_book)
        session.commit()
        return "ok", 200


    @app.route("/take-book", methods=["POST"])
    def refund_book():
        """
        ID в базе изменяются после каждого запуска скрипта
        """
        book_id = request.form.get("book_id", type=int)
        student_id = request.form.get("student_id", type=int)
        try:
            date_of_issue = session.query(ReceivingBooks.date_of_issue).filter(
                ReceivingBooks.student_id == student_id).filter(ReceivingBooks.book_id == book_id).one()
        except NoResultFound:
            return abort(403, "Forbidden - ID not correct!")
        date_of = None
        for i in date_of_issue:
            date_of = i
        refund_book = ReceivingBooks(
            book_id=book_id,
            student_id=student_id,
            date_of_issue=datetime.date.fromisoformat(str(date_of)),
            date_of_return=datetime.date.today(),
        )
        session.add(refund_book)
        session.commit()
        return "ok", 200


    def init_db():
        try:
            os.remove("homework.db")
        except Exception:
            pass
        Base.metadata.create_all(bind=engine)
        for _ in range(20):
            books = Books(
                author_id=random.randint(1, 10),
                realese_date=get_random_date(),
                name=random.choice(book_names).strip(),
            )
            session.add(books)
        for _ in range(10):
            authors = Authors(
                surname=random.choice(last_names).strip(),
                name=random.choice(middle_names).strip(),
            )
            session.add(authors)
        for _ in range(200):
            students = Students(
                surname=random.choice(last_names).strip(),
                name=random.choice(first_names).strip(),
                email=generate_email(),
                phone=generate_phone(),
                average_score=random.randint(2, 5),
                scholarship=bool(random.getrandbits(1)),
            )
            session.add(students)
        for _ in range(200):
            receiving_books = ReceivingBooks(
                book_id=random.randint(1, 20),
                student_id=random.randint(1, 200),
                date_of_issue=get_random_date(),
                date_of_return=random.choice([None, get_random_date()]),
            )
            session.add(receiving_books)
        session.commit()


    init_db()
    app.config['JSON_AS_ASCII'] = False
    app.run()
