"""
Иногда бывает важно сгенерировать какие то табличные данные по заданным характеристикам.
К примеру, если вы будете работать тестировщиками, вам может потребоваться добавить
    в тестовую БД такой правдоподобный набор данных (покупки за сутки, набор товаров в магазине,
    распределение голосов в онлайн голосовании).

Давайте этим и займёмся!

Представим, что наша FrontEnd команда делает страницу сайта УЕФА с жеребьевкой команд
    по группам на чемпионате Европы.

Условия жеребьёвки такие:
Есть N групп.
В каждую группу попадает 1 "сильная" команда, 1 "слабая" команда и 2 "средние команды".

Задача: написать функцию generate_data, которая на вход принимает количество групп (от 4 до 16ти)
    и генерирует данные, которыми заполняет 2 таблицы:
        1. таблицу со списком команд (столбцы "номер команды", "Название", "страна", "сила команды")
        2. таблицу с результатами жеребьёвки (столбцы "номер команды", "номер группы")

Таблица с данными называется `uefa_commands` и `uefa_draw`
"""
import sqlite3
import random
from pprint import pprint

import requests
from bs4 import BeautifulSoup


def get_countries(headers, url):
    """
    Парсит список стран из википедии

    """
    response = requests.get(url, headers=headers, timeout=3)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "lxml")
    prepare_total = soup.select(".wikitable .image")
    try:
        for i in prepare_total:
            countries.append(i["title"])
    except KeyError as exc:
        pass


def generate_collect_team(countries):
    """
    Создает данные команд, сделал словарь для наглядности и проверки корректности данных

    """
    collect_team = []
    for number in range(1, len(team_names)):
        country = random.choice(countries)
        # делаю словарь для теста структуры
        collect_team.append(
            {
                "number_team": number,
                "name_team": random.choice(team_names),
                "country_team": country,
                "level_team": random.choice(["high", "medium", "low"])
            }
        )
        # удаляю страну из списка чтобы не повторялось
        if country in countries:
            countries.remove(country)
    return collect_team


def wrire_db_team(collect_team, c: sqlite3.Cursor, sql_insert_commands_request):
    """
    Записывает команду в таблицу `uefa_commands`

    """
    for item in collect_team:
        c.execute(sql_insert_commands_request, (
            item["number_team"],
            item["name_team"],
            item["country_team"],
            item["level_team"]
        )
                  )


def generate_groups(collect_team, number_of_groups, connect: sqlite3.Cursor, sql_insert_groups):
    """
    Создает группы команд по критериям уровней: "high", "medium", "medium", "low"

    """
    for group in range(1, number_of_groups + 1):
        while True:
            collect_group = []
            for team in collect_team:
                if team["level_team"] == "medium":
                    team["group_team"] = group
                    collect_group.append(team)
                    collect_team.remove(team)
                    for team in collect_team:
                        if team["level_team"] == "medium":
                            team["group_team"] = group
                            collect_group.append(team)
                            collect_team.remove(team)
                            break
                    break
            for team in collect_team:
                if team["level_team"] == "high":
                    team["group_team"] = group
                    collect_group.append(team)
                    collect_team.remove(team)
                    break
            for team in collect_team:
                if team["level_team"] == "low":
                    team["group_team"] = group
                    collect_group.append(team)
                    collect_team.remove(team)
                    break
            break
        write_groups(collect_group, connect, sql_insert_groups)


def write_groups(collect_group, connect, sql_insert_groups):
    """
    Записывает группу в таблицу `uefa_draw`

    """
    try:
        for team in collect_group:
            connect.execute(sql_insert_groups, (team["number_team"], team['group_team'],))
    except sqlite3.IntegrityError:
        pass
    pprint(collect_group)


if __name__ == "__main__":
    countries = []
    team_names = [
                     "Команда B",
                     "Неуспевающие",
                     "Бэби-бумеры",
                     "Отсев из колледжа",
                     "Низкие ожидания",
                     "Дно бочки",
                     "Самые слабые звенья",
                     "Комплекс неполноценности",
                     "Что-нибудь безобидное",
                     "Эпические неудачи",
                     "Деревенские идиоты",
                     "Второе место",
                     "Пакет расширения",
                     "Гражданское неповиновение",
                     "Огнетушители",
                     "Золотоискатели",
                     "Чудеса с одним ударом",
                     "Проспавшие",
                 ] * 8
    sql_insert_commands = """
                   INSERT INTO
                       'uefa_commands' (command_number, command_name, command_country, command_level)
                   VALUES
                       (?, ?, ?, ?);
                   """
    sql_request_all = """
        SELECT * FROM uefa_commands
    """
    sql_insert_groups = """
                       INSERT INTO
                           'uefa_draw' (command_number, group_number)
                       VALUES
                           (?, ?);
                       """
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)"
                      " Chrome/96.0.4{}.{} Safari/537.36",
    }
    url = "https://ru.wikipedia.org/" \
          "wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B3%D0%BE%D1%81%D1%83%D0%B4%D0%B0%D1%80%D1%81%D1%82%D0%B2"
    get_countries(headers, url)

    number_of_groups = int(input("Введите количество групп (от 4 до 16ти): "))
    while True:
        if 4 <= number_of_groups <= 16:
            break
        number_of_groups = int(input("Введите количество групп (от 4 до 16ти): "))

    collect_team = generate_collect_team(countries)
    with sqlite3.connect("hw.db") as conn:
        cursor = conn.cursor()
        try:
            wrire_db_team(collect_team, cursor, sql_insert_commands)
        except sqlite3.IntegrityError:
            pass

    with sqlite3.connect("hw.db") as conn:
        cursor = conn.cursor()
        generate_groups(collect_team, number_of_groups, cursor, sql_insert_groups)
