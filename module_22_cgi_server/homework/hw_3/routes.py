import time

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/long_task')
def long_task():
    time.sleep(300)
    return jsonify(message='We did it!')


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False, port=80)
