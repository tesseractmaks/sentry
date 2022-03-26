import datetime
import time
import logging
import threading
import collections
from threading import Lock

import requests


def get_content():
    global date_entries

    start = time.time()
    working_time = 20
    url = 'https://showcase.api.linx.twenty57.net/UnixTime/fromunix'
    while True:
        timestamp = datetime.datetime.now().timestamp().__round__()
        param = {'timestamp': timestamp}
        with LOCK:
            time.sleep(1)
            response = requests.get(url, params=param, timeout=3)
            response.raise_for_status()
            date_record = response.json()
            date_entries[f'{date_record}'] = threading.Thread().getName()
            time_check = time.time() - start
        if time_check.__round__() >= working_time:
            break
        break


def worker():
    count_thread = 0
    for i in range(10):
        time.sleep(1)
        thread = threading.Thread(target=get_content)
        thread.start()
        count_thread += 1
        print(f'№ {count_thread} {threading.Thread().getName()}')
        thread.join()
    print('ok')


if __name__ == '__main__':
    logging.basicConfig(filename='applog.log', filemode='w', level='INFO')
    logger = logging.getLogger(__name__)
    LOCK = Lock()
    date_entries = {}
    worker()
    entries_sort = collections.OrderedDict(sorted(date_entries.items()))
    for date, thread in entries_sort.items():
        logger.info(f'{thread} {date}')
