import unittest

from flask import request
from hw.hw_1_2 import app


class TestRegistrationForm(unittest.TestCase):

    def create_app(self):
        app.config.from_object('config.TestConfiguration')
        return app

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.request_context = app.test_request_context(
            '/registration/?email=test@rty.ru&phone=8999121545&name=qwerty&address=qwedrtyaddress&index=77'
        )

    def test_email(self):
        with self.request_context:
            self.assertEqual(request.args['email'], 'test@rty.ru')

    def test_phone(self):
        with self.request_context:
            self.assertEqual(request.args['phone'], '8999121545')

    def test_name(self):
        with self.request_context:
            self.assertEqual(request.args['name'], 'qwerty')

    def test_address(self):
        with self.request_context:
            self.assertEqual(request.args['address'], 'qwedrtyaddress')

    def test_index(self):
        with self.request_context:
            self.assertEqual(request.args['index'], '77')






