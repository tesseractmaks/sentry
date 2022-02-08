from flask import Flask

from logging_config import CustomFileHandler

app = Flask(__name__)


@app.route("/logs", methods=["POST"])
def published():
    res = CustomFileHandler.message
    return res


if __name__ == '__main__':
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)



