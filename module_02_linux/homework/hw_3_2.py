"""
Давайте напишем свое приложение для учета финансов.
Оно должно уметь запоминать, сколько денег мы потратили за день,
    а также показывать затраты за отдельный месяц и за целый год.

Модифицируйте  приведенный ниже код так, чтобы у нас получилось 3 endpoint:
/add/<date>/<int:number> - endpoint, который сохраняет информацию о совершённой за какой-то день трате денег (в рублях, предполагаем что без копеек)
/calculate/<int:year> -- возвращает суммарные траты за указанный год
/calculate/<int:year>/<int:month> -- возвращает суммарную трату за указанный месяц

Гарантируется, что дата для /add/ endpoint передаётся в формате
YYYYMMDD , где YYYY -- год, MM -- месяц (число от 1 до 12), DD -- число (от 01 до 31)
Гарантируется, что переданная дата -- корректная (никаких 31 февраля)
"""
import datetime
import calendar
import re

from flask import Flask

app = Flask(__name__)

storage = {}


@app.route("/add/<date>/<int:number>")
def add(date, number):

    try:
        if re.findall(r"\b[\d+]{8}\b", date):
            date_iso = "%s-%s-%s" % (date[0:4], date[4:6], date[6:8])
    except ValueError("Дата передаётся в формате YYYYMMDD,") as exc:
        raise exc
    except ValueError as exc:
        raise exc
    try:
        datetime_object = datetime.datetime.strptime(date_iso, '%Y-%m-%d')
    except ValueError as exc:
        raise exc
    storage["date"] = datetime_object
    storage["number"] = number
    return f"{storage['date']} {storage['number']}"


@app.route("/calculate/<int:year>")
def calculate_year(year):
    current = datetime.date.today()
    user_date_plus_one = datetime.date(year=storage["date"].year + 1, month=1, day=1)
    user_date = datetime.date(year=year, month=1, day=1)

    if current.year == user_date.year:
        current_year_delta_days = current - user_date
        return f"Суммарные траты за {year} год: {str(current_year_delta_days.days * int(storage['number'])).split()[0]} рублей"
    else:
        other_year_delta_days = user_date_plus_one - user_date
        return f"Суммарные траты за {year} год: {str(other_year_delta_days.days * int(storage['number'])).split()[0]} рублей"


@app.route("/calculate/<int:year>/<int:month>")
def calculate_month(year, month):
    days = calendar.monthrange(year, month)
    return f"Суммарные траты за {year}-{month}: {days[1] * int(storage['number'])} рублей"


if __name__ == "__main__":
    app.run(debug=True)
