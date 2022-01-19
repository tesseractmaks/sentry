import shlex
import subprocess

from flask import Flask, request



# if __name__ == '__main__':
app = Flask(__name__)


@app.route("/host/")
def get_uptime():
    return f"Current host is:{request.host} "

port = 5000

app.run(debug=True, port=port)










