import os

from flask import Flask, render_template, send_from_directory

root_dir = os.path.dirname(os.path.abspath(__file__))

template_folder = os.path.join(root_dir, "static")

app = Flask(__name__, template_folder=template_folder)
HOST = '0.0.0.0'
PORT = 5000


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/static/<path:path>")
def send_static(path):
    return send_from_directory(template_folder, path)


if __name__ == "__main__":
    app.run(host=HOST, port=PORT)

