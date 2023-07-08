from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy import func, create_engine, Column, Integer, String, Date, Float, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship, backref
from sqlalchemy.ext.hybrid import hybrid_property

import datetime

engine = create_engine("sqlite:///homework.db")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Author(Base):
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


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    count = Column(Integer, default=1)
    realese_date = Column(Date, nullable=False)

    author_id = Column(Integer, ForeignKey("authors.id"))
    author = relationship("Author", backref=backref("books", cascade=("all", "delete-orphan"), lazy="select", ))

    student_relation = relationship("ReceivingBooks", backref="books")
    students = association_proxy("student_relation", "students")

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
            book = session.query(Book).filter(Book.name.contains(name)).all()
            return book
        except Exception:
            pass


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    phone = Column(String(10), nullable=False)
    email = Column(String(50), nullable=False)
    average_score = Column(Float, nullable=False)
    scholarship = Column(Boolean, nullable=False)

    book_relation = relationship("ReceivingBooks", backref="students")
    books = association_proxy("book_relation", "books")

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
        return session.query(Student).filter(Student.scholarship == True).all()

    @classmethod
    def get_average_score_higher(cls, avg_score):
        return session.query(Student).filter(Student.average_score > avg_score).all()


class ReceivingBooks(Base):
    __tablename__ = "receiving_books"

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey("books.id"))
    student_id = Column(Integer, ForeignKey("students.id"))
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
