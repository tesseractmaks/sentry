import sqlite3

import requests
import threading
import time

from requests import HTTPError
from itertools import count


def get_content():
    url = 'https://swapi.dev/api/people/'
    param = {}
    for page in count(1):
        param["page"] = page
        response = requests.get(url, params=param)
        response.raise_for_status()
        people_content = response.json()['results']
        for people in people_content:
            try:
                yield people
            except IndexError:
                break


class StarWarsPeople(threading.Thread):
    def __init__(self, people, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.people = people

    def run(self):
        people = self.people

        with sqlite3.connect("Obi_Wan.db") as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO people(name, birth_year, gender) VALUES(?, ?, ?);",
                (people['name'], people['birth_year'], people['gender'])
            )
            conn.commit()


if __name__ == '__main__':
    start = time.time()
    count_people = 0
    try:
        for people in get_content():
            object_thread = StarWarsPeople(people=people)
            object_thread.start()
            count_people += 1
            if count_people == 20:
                break
    except HTTPError:
        pass
    except(KeyError):
        pass
    end = time.time()
    print((end - start).__round__(3), 'sec.')










