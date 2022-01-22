"""
Логов бывает очень много. А иногда - ооооооооочень много.
Из-за этого люди часто пишут логи не в человекочитаемом,
    а в машиночитаемом формате, чтобы машиной их было обрабатывать быстрее.

Напишите функцию

def log(level: str, message: str) -> None:
    pass


которая будет писать лог  в файл skillbox_json_messages.log в следующем формате:
{"time": "<время>", "level": "<level>", "message": "<message>"}

сообщения должны быть отделены друг от друга символами переноса строки.
Обратите внимание: наше залогированное сообщение должно быть валидной json строкой.

Как это сделать? Возможно метод json.dumps поможет вам?
"""

import json
import datetime


def log(level: str, message: str) -> None:
    time = datetime.datetime.now()
    logger = json.dumps(
        {
            "time": datetime.datetime.strftime(time, "%Y:%m:%d %H:%M:%S"),
            "level": level,
            "message": message
        },
        indent=4
    )
    print(logger)


for test in range(10):
    log(f"{test}", f"{test}")
