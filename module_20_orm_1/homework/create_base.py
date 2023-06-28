import string

import datetime
import random

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
    Книга Соловьёвича
    """.split(',')


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

