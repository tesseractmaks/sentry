import time
from concurrent.futures import ThreadPoolExecutor

import requests
import logging

logging.basicConfig(level=logging.DEBUG)


class BookClient():
    URL: str = 'http://0.0.0.0:5000/api/books'
    TIMEOUT: int = 5
    session = requests.Session()

    def __int__(self, qweries, sessions, threads):
        self.qweries = qweries
        self.sessions = sessions
        self.threads = threads

    def get_all_books(self, sessions):
        if sessions:
            response = self.session.get(self.URL, timeout=self.TIMEOUT)
            return response.json()
        response = requests.get(self.URL, timeout=self.TIMEOUT)
        return response.json()

    def start_by_threads(self, qweries=10, sessions=False):
        with ThreadPoolExecutor(5) as executor:
            try:
                for _ in range(qweries):
                    future = executor.submit(self.get_all_books, sessions)
                    end = time.time()
                    data = future.done()
            except Exception as exc:
                logging.error(exc)


def main(qweries=10, sessions=False, threads=False):
    client = BookClient()
    start = time.time()
    if threads:
        client.start_by_threads(qweries=qweries, sessions=sessions)

    for _ in range(qweries):
        client.get_all_books(sessions=sessions)
    end = time.time()
    print("threads - ", bool(threads))
    print("session - ", bool(sessions))
    print((end - start).__round__(4), 'sec.')


if __name__ == '__main__':
    main(qweries=10, sessions=True, threads=False)




