import datetime
import re
import unittest
import calendar

from module_02_linux.homework.hw_3_2 import app


class TestCalculate(unittest.TestCase):
    storage = {
        "date": "20210110",
        "number": "200",
    }
    date_iso = "%s-%s-%s" % (storage["date"][0:4], storage["date"][4:6], storage["date"][6:8])

    def setUp(self):
        self.datetime_object = datetime.datetime.strptime(self.date_iso, '%Y-%m-%d')
        self.datetime_str = datetime.datetime.strftime(self.datetime_object, '%Y-%m-%d')
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app_context = app.app_context()
        self.app_context.push()
        self.app = app.test_client()

    def test_add(self):
        base_url = "/add/"
        response = self.app.get(f"{base_url + self.storage['date']}/{self.storage['number']}")
        response_text = response.data.decode()
        self.assertTrue(self.datetime_str in response_text)
        self.assertTrue(self.storage['number'] in response_text)

    def calculate_year(self):
        year = self.datetime_object.year
        current = datetime.date.today()
        user_date_plus_one = datetime.date(year=self.datetime_object.year + 1, month=1, day=1)
        user_date = datetime.date(year=year, month=1, day=1)
        if current.year == user_date.year:
            current_year_delta_days = current - user_date
            return f"{str(current_year_delta_days.days * int(self.storage['number'])).split()[0]}"
        else:
            other_year_delta_days = user_date_plus_one - user_date
            return f"{str(other_year_delta_days.days * int(self.storage['number'])).split()[0]}"

    def test_calculate_year(self):
        calculate = self.calculate_year()
        base_url = "/calculate/"
        year = str(self.datetime_object.year)
        response = self.app.get(f"{base_url}{year}")
        response_text = response.data.decode()
        self.assertTrue(year in response_text)
        self.assertEqual(calculate, '73000')

    def test_calculate_month(self):
        base_url = "/calculate/"
        year = self.datetime_object.year
        month = self.datetime_object.month
        days = calendar.monthrange(year, month)
        calculate_month = days[1] * int(self.storage['number'])
        response = self.app.get(f"{base_url}{year}/{month}")
        response_text = response.data.decode()
        self.assertTrue(str(year) in response_text)
        self.assertTrue(str(month) in response_text)
        self.assertEqual(calculate_month, 6200)

    def test_add_validate_date(self):
        valid_date = re.search(r"\b[\d+]{8}\b", self.storage['date']).group()
        self.assertEqual(valid_date, self.storage['date'])

    def test_add_no_valid_date(self):
        storage = {
            "date": "20210170",
            "number": "200",
        }
        base_url = "/add/"
        with self.assertRaises(ValueError):
            response = self.app.get(f"{base_url + storage['date']}/{storage['number']}")
            response_text = response.data.decode()
            app.add(response_text)

    def test_add_without_parameters(self):
        storage = {
            "date": "",
            "number": "",
        }
        base_url = "/add/"
        with self.assertRaises(AttributeError):
            response = self.app.get(f"{base_url + storage['date']}/{storage['number']}")
            response_text = response.data.decode()
            app.add(response_text)















































# storage = {}
#
#
# @app.route("/add/<date>/<int:number>")
# def add(date, number):
#     date_iso = "%s-%s-%s" % (date[0:4], date[4:6], date[6:8])
#     datetime_object = datetime.datetime.strptime(date_iso, '%Y-%m-%d')
#     storage["date"] = datetime_object
#     storage["number"] = number
#     return f"{storage['date']} {storage['number']}"
#
#
# @app.route("/calculate/<int:year>")
# def calculate_year(year):
#
#     current = datetime.date.today()
#     user_date_plus_one = datetime.date(year=storage["date"].year + 1, month=1, day=1)
#     user_date = datetime.date(year=year, month=1, day=1)
#
#     if current.year == user_date.year:
#         current_year_delta_days = current - user_date
#         return f"Суммарные траты за {year} год: {str(current_year_delta_days.days * int(storage['number'])).split()[0]} рублей"
#     else:
#         other_year_delta_days = user_date_plus_one - user_date
#         return f"Суммарные траты за {year} год: {str(other_year_delta_days.days * int(storage['number'])).split()[0]} рублей"
#
#
# @app.route("/calculate/<int:year>/<int:month>")
# def calculate_month(year, month):
#     days = calendar.monthrange(year, month)
#     return f"Суммарные траты за {year}-{month}: {days[1] * int(storage['number'])} рублей"
#
#
# if __name__ == "__main__":
#     app.run(debug=True)
