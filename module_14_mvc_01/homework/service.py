import json
import sqlite3
import random

from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired

app = Flask(__name__)

# @app.route('/books/author', methods=["GET", "POST"])
# def get_result_search_books():
#     author_name = request.form.get("author_name")
#     get_data = """
#                SELECT * FROM table_books WHERE author = ?;
#            """
#     count_views = """
#     UPDATE table_books SET count_views = count_views + 1 WHERE author = ?;
#     """
#     with sqlite3.connect("table_books.db") as conn:
#         cursor = conn.cursor()
#         cursor.execute(get_data, (str(author_name), ))
#         data_sql = cursor.fetchone()
#         cursor.execute(count_views, (str(author_name),))
#         data = dict(zip(("id", "title", "author", "count_views"), data_sql))
#     return render_template('search_result_book.html', data=data)

ROOMS = [
    {'floor': 1, 'beds': 2, 'guestNum': 10, 'price': 1000},
    {'floor': 2, 'beds': 2, 'guestNum': 20, 'price': 700},
    {'floor': 3, 'beds': 1, 'guestNum': 3, 'price': 500},
    {'floor': 4, 'beds': 2, 'guestNum': 7, 'price': 800},
    {'floor': 1, 'beds': 4, 'guestNum': 12, 'price': 1400},
]
first_names = ['Август', 'Августин', 'Авраам', 'Аврора', 'Агата', 'Агафон']
last_names = ['Карпова', 'Матвеева', 'Медведева', 'Белая', 'Полякова', 'Фролова']
BOOKINGS = [
    {'checkIn': int(f"2021030{random.randint(1, 8)}"), 'checkOut': int(f"202103{random.randint(11, 20)}"),
     'firstName': random.choice(first_names), 'lastName': random.choice(last_names), 'roomId': 1},
    {'checkIn': int(f"2021030{random.randint(1, 8)}"), 'checkOut': int(f"202103{random.randint(11, 20)}"),
     'firstName': random.choice(first_names), 'lastName': random.choice(last_names), 'roomId': 2},
    {'checkIn': int(f"2021030{random.randint(1, 8)}"), 'checkOut': int(f"202103{random.randint(11, 20)}"),
     'firstName': random.choice(first_names), 'lastName': random.choice(last_names), 'roomId': 3},
]


def init_db(ROOMS, BOOKINGS):
    with sqlite3.connect('booking.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='rooms';"
            # "SELECT name FROM sqlite_master WHERE type='table' AND name='booking';"
        )
        exists = cursor.fetchone()

        if not exists:
            cursor.executescript(
                'CREATE TABLE `rooms`'
                '(id INTEGER PRIMARY KEY AUTOINCREMENT, floor INTEGER, beds INTEGER, guestNum INTEGER, price INTEGER)'
            )

            cursor.executescript(
                'CREATE TABLE `booking_rooms`'
                '(id INTEGER PRIMARY KEY AUTOINCREMENT, checkIn INTEGER, checkOut INTEGER, firstName TEXT,'
                ' lastName TEXT, roomId INTEGER NOT NULL, FOREIGN KEY (roomId) REFERENCES room(id))'
            )

            cursor.executemany(
                """INSERT INTO rooms (floor, beds, guestNum, price) VALUES (?, ?, ?, ?);""",
                [(item['floor'], item['beds'], item['guestNum'], item['price']) for item in ROOMS]
            )

            cursor.executemany(
                """INSERT INTO booking_rooms (checkIn, checkOut, firstName, lastName, roomId) VALUES (?, ?, ?, ?, ?);""",
                [(item['checkIn'], item['checkOut'], item['firstName'], item['lastName'], item['roomId']) for item in BOOKINGS]
            )


@app.route('/add-room', methods=["POST"])
def addRoom():
    get_data = """SELECT * FROM rooms"""
    with sqlite3.connect("booking.db") as conn:
        cursor = conn.cursor()
        cursor.execute(get_data)
        res = cursor.fetchall()
    return res


@app.route('/room', methods=["GET"])
def GetRoom():
    get_data = """SELECT * FROM booking_rooms WHERE checkIn = ? AND checkOut = ? AND :guestsNum = ?; """

    result = request.args.to_dict()
    print(result)
    with sqlite3.connect("booking.db") as conn:
        cursor = conn.cursor()
        cursor.execute(get_data, (result['checkIn'], result['checkOut'], result['guestsNum'], ))
        result = cursor.fetchone()

    print(result)
    return result


@app.route('/booking', methods=["POST"])
def Booking():
    result = request.get_data()
    return result


if __name__ == '__main__':
    init_db(ROOMS, BOOKINGS)
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)

    # "header": [
	# 				{
	# 					"key": "Content-Type",
	# 					"value": "application/json",
	# 					"type": "json"
	# 				}
	# 			],