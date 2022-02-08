from flask import Flask

app = Flask(__name__)


@app.route("/logs", methods=["POST"])
def published():
    return "Ok"


if __name__ == '__main__':
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)



