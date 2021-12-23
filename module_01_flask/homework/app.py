import datetime
import random

from flask import Flask

app = Flask(__name__)

list_count = []


@app.route('/hello_world')
def get_hello_world():
    return 'Hello World', list_count.append(1)


@app.route('/cars')
def get_cars():
    return 'Chevrolet, Renault, Ford, Lada', list_count.append(1)


@app.route('/cats')
def get_cats():
    cats = [
        'корниш рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин'
    ]
    return random.choice(cats), list_count.append(1)


@app.route('/get_time/now')
def test_function():
    return f'{datetime.datetime.now()}', list_count.append(1)


@app.route('/get_time/future')
def get_time():
    return f'Точное время через час будет: {datetime.datetime.now() + datetime.timedelta(hours=1)}', \
           list_count.append(1)


@app.route('/get_random_word')
def get_random():
    with open('voyna-i-mir.txt', encoding='cp1251') as file:
        return random.choice(str(list(file)).split(' ')), list_count.append(1)


@app.route('/counter')
def get_counter():
    return f'Страница открывалась {len(list_count)} раз'


if __name__ == "__main__":
    app.run(debug=True)