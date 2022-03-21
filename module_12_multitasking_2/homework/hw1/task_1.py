import sqlite3
import time

import requests

from multiprocessing.pool import ThreadPool
from requests import HTTPError
from itertools import count


def get_content():
    url = 'https://swapi.dev/api/people/'
    param = {}
    people_collection = []
    flag_stop = False
    count_people = 0
    for page in count(1):
        param["page"] = page
        response = requests.get(url, params=param)
        response.raise_for_status()
        people_content = response.json()['results']
        for people in people_content:
            try:
                if count_people == 20:
                    flag_stop = True
                    break
                people_collection.append(people)
            except IndexError:
                break
            count_people += 1
        if flag_stop:
            return people_collection


def records(people):
    with sqlite3.connect("Obi_Wan.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO people(name, birth_year, gender) VALUES(?, ?, ?);",
            (people['name'], people['birth_year'], people['gender'])
        )
        conn.commit()


if __name__ == '__main__':
    start = time.time()
    try:
        people_collection = get_content()
    except HTTPError:
        pass
    except(KeyError):
        pass
    with ThreadPool(processes=3) as pool:
        people = pool.map_async(records, people_collection)
        people.wait(timeout=5)
    end = time.time()
    print((end - start).__round__(3), 'sec.')


