"""
Напишите GET flask endpoint с url /uptime,
    который в ответ на запрос будет возвращать как долго текущая машина не перезагружалась
        (в виде строки f"Current uptime is '{UPTIME}'"
            где UPTIME - uptime системы. Это можно сделать с помощью команды uptime
            (https://www.opennet.ru/man.shtml?topic=uptime&category=1&russian=4)
        )

Напомним, что вызвать программу из python можно с помощью модуля subprocess:

"""

import shlex, subprocess

from flask import Flask

app = Flask(__name__)


@app.route("/uptime/")
def get_uptime():
    command_str = f"uptime"
    command = shlex.split(command_str)
    result = subprocess.run(command, capture_output=True)
    return f"Current uptime is: '{result.stdout}'"


if __name__ == "__main__":
    app.run(debug=True)








