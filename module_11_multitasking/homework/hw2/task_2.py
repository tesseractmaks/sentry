import sqlite3

import requests
import time

from requests import HTTPError
from itertools import count


def get_content():
    start = time.time()
    count_people = 1
    url = 'https://swapi.dev/api/people/'
    param = {}
    for page in count(1):
        param["page"] = page
        response = requests.get(url, params=param)
        response.raise_for_status()
        people_content = response.json()['results']
        for people in people_content:
            with sqlite3.connect("Obi_Wan.db") as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO people(name, birth_year, gender) VALUES(?, ?, ?);",
                    (people['name'], people['birth_year'], people['gender'])
                )
                conn.commit()
            try:
                count_people += 1
            except IndexError:
                break
            if count_people == 21:
                break
        if count_people == 21:
            break
    end = time.time()
    print((end - start).__round__(3))


if __name__ == '__main__':
    try:
        get_content()
    except HTTPError:
        pass
    except(KeyError):
        pass





