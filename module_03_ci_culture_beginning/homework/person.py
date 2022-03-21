import datetime


class Person:
    def __init__(self, name, year_of_birth, address=''):
        self.name = name
        self.yob = year_of_birth
        self.address = address

    def get_age(self):
        now = datetime.datetime.now()
        year_of_birth = datetime.datetime.strptime(self.yob, '%Y-%m-%d')
        return now.year - year_of_birth.year

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
        return self.name

    def set_address(self, address):
        self.address = address
        return self.address

    def get_address(self):
        return self.address

    def is_homeless(self):
        '''
        returns True if address is not set, false in other case
        '''
        if self.address is None:
            return True
        else:
            return False



