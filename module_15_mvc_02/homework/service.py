import json
import sqlite3
from flask import Flask, request, make_response, jsonify

app = Flask(__name__)


def init_db():
    with sqlite3.connect('booking.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='rooms';"
        )
        exists = cursor.fetchone()
        if not exists:
            cursor.executescript(
                'CREATE TABLE `rooms`'
                '(id INTEGER PRIMARY KEY AUTOINCREMENT, floor INTEGER, beds INTEGER, guestNum INTEGER, price INTEGER, '
                'checkIn INTEGER, checkOut INTEGER, firstName TEXT,lastName TEXT, roomId INTEGER)'
            )


@app.route('/add-room', methods=["POST"])
def addRoom():
    get_data = """SELECT * FROM rooms"""
    with sqlite3.connect("booking.db") as conn:
        cursor = conn.cursor()
        cursor.execute(get_data)
        res = cursor.fetchall()
    return res


def room_is_free(room, check_in, check_out):
    get_data = """SELECT roomId FROM rooms WHERE checkIn = ? AND checkOut = ?"""
    with sqlite3.connect("booking.db") as conn:
        cursor = conn.cursor()
        cursor.execute(get_data, (check_in, check_out, ))
        rooms = [room[0] for room in cursor.fetchall()]
        if room in rooms:
            return room


def booking_rooms(booking):
    check_in = booking['bookingDates']['checkIn']
    check_out = booking['bookingDates']['checkOut']
    first_name = booking['firstName']
    last_name = booking['lastName']
    room = booking['roomId']
    get_data = """INSERT INTO rooms (checkIn, checkOut, firstName, lastName, roomId) VALUES (?, ?, ?, ?, ?)"""
    if room_is_free(room, check_in, check_out):
        with sqlite3.connect("booking.db") as conn:
            cursor = conn.cursor()
            cursor.execute(get_data, (int(check_in), int(check_out), first_name, last_name, int(room),))
            rooms = [room[0] for room in cursor.fetchall()]
        return rooms


@app.route('/room', methods=["GET"])
def GetRoom():
    result = request.args.to_dict()
    return result


@app.route('/booking', methods=["POST"])
def Booking():
    if booking_rooms('booking-service.postman_collection.json'):
        return make_response('Booking Successfull!', 200)
    return make_response('Room is already booked!', 409)


if __name__ == '__main__':
    init_db()
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)

