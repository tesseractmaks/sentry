import string
import datetime
import random
import os
import csv

from models import \
    Book, \
    ReceivingBooks, \
    Author, Student, \
    Base, \
    session, \
    engine

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


def book_names():
    names = """
            Книга Иваныча,
            Книга Василича,
            Книга Петровича,
            Книга Смирновича,
            Книга Соловьёвича,
            """.split(',')
    for name in range(20):
        book_name = random.choice(names[:-1]) + random.choice(string.ascii_letters)
        return book_name.strip()


def get_random_date():
    start_date = datetime.date(2023, 5, 10)
    end_date = datetime.date.today()
    num_days = (end_date - start_date).days
    rand_days = random.randint(1, num_days)
    random_date = start_date + datetime.timedelta(days=rand_days)
    return random_date


def generate_phone():
    one = str(random.randint(1, 123)).zfill(3)
    two = str(random.randint(0, 789)).zfill(3)
    return "8-495-{}-{}".format(one, two)


def generate_email():
    servers = ['@gmail', '@yahoo', '@redmail', '@hotmail', '@bing']
    tlds = ['.com', '.in', '.gov', '.ac.in', '.net', '.org']
    username = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(4, 11)))
    return username + random.choice(servers) + random.choice(tlds)


def init_db():
    try:
        os.remove("homework.db")
    except Exception:
        pass
    try:
        os.remove("staticFiles/test_students.csv")
    except Exception:
        pass
    Base.metadata.create_all(bind=engine)

    for i in range(10):
        authors = Author(
            surname=random.choice(last_names).strip(),
            name=random.choice(middle_names).strip(),
        )
        session.add(authors)
    session.commit()

    for i in range(30):
        books = Book(
            author_id=random.randint(1, 10),
            realese_date=get_random_date(),
            name=book_names(),
        )
        session.add(books)

    session.commit()
    for _ in range(200):
        students = Student(
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
            student_id=random.randint(1, 8),
            date_of_issue=get_random_date(),
            date_of_return=random.choice([None, get_random_date()]),
        )
        session.add(receiving_books)
    session.commit()
    create_file_students()


def create_file_students():
    students = session.query(Student.name,
                             Student.surname,
                             Student.phone,
                             Student.email,
                             Student.average_score,
                             bool(Student.scholarship),
                             ).all()

    with open("test_students.csv", "w", newline="") as file:
        headers = [column.key for column in Student.__table__.columns]
        writer = csv.writer(file, delimiter=";")
        writer.writerow(headers[1:])
        for row in students:
            writer.writerow(row)
