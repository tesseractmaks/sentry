import datetime
import unittest

from homework.person import Person


class TestPerson(unittest.TestCase):

    def setUp(self):
        year_of_birth = "2001-01-01"
        self.name = "Mikolka"
        self.yob = year_of_birth
        self.address = ""
        self.man = Person(year_of_birth=year_of_birth, name=self.name, address=self.address)

    def test_get_age(self):
        now = datetime.datetime.now()
        year_of_birth = datetime.datetime.strptime(self.yob, '%Y-%m-%d')
        age = now.year - year_of_birth.year
        self.assertEqual(self.man.get_age(), age)

    def test_get_name(self):
        self.assertEqual(self.man.get_name(), self.name)

    def test_set_name(self):
        self.assertEqual(self.man.set_name(self.name), self.name)

    def test_set_address(self):
        self.assertEqual(self.man.set_address(self.address), self.address)

    def test_get_address(self):
        self.assertEqual(self.man.get_address(), self.address)

    def test_is_homeless(self):
        if self.address is None:
            self.assertTrue(self.man.is_homeless() is True)
        else:
            self.assertTrue(self.man.is_homeless() is False)
