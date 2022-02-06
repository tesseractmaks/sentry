import sys
from flask import Flask
from app import calc

app = Flask(__name__)


@app.route("/logs", methods=["POST"])
def published():
    # TODO здесь вызываю основной код из которого должен получить строки логгеров
    stdout = calc(sys.argv[1:])
    return f'<pre> {stdout} </pre>'


if __name__ == '__main__':
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)

