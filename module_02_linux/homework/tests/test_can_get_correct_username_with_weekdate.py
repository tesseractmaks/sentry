import datetime
import unittest

from module_02_linux.homework.hw_2_4_hello_world_with_day import app


class TestWeekDate(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/hello-world/'

    def test_correct_username(self):
        username = 'username'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(username in response_text)

    def test_correct_weekday(self):
        username = 'username'
        day = datetime.datetime.today().weekday()
        week = {
            0: 'Хорошего Понедельника',
            1: 'Хорошего Вторника',
            2: 'Хорошей Среды',
            3: 'Хорошего Четверга',
            4: 'Хорошей Пятницы',
            5: 'Хорошей Субботы',
            6: 'Хорошего Воскресенья',
        }
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(week[day] in response_text)







