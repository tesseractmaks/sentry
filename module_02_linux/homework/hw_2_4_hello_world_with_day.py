"""
Напишите  hello-world endpoint , который возвращал бы строку "Привет, <имя>. Хорошей пятницы!".
Вместо хорошей пятницы, endpoint должен уметь желать хорошего дня недели в целом, на русском языке.
Текущий день недели можно узнать вот так:
"""
import datetime

from flask import Flask

app = Flask(__name__)


@app.route("/hello-world/<username>")
def hello_world(username):
    day = datetime.datetime.today().weekday()
    week = {
        0: 'Хорошего Понедельника',
        1: 'Хорошего Вторника',
        2: 'Хорошей Среды',
        3: 'Хорошего Четверга',
        4: 'Хорошей Пятницы',
        5: 'Хорошей Субботы',
        6: 'Хорошего Воскресенья',
    }

    return f"Привет, {username}. {week[day]}!"


if __name__ == "__main__":
    app.run(debug=True)
