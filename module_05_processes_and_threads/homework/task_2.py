import os
import shlex, subprocess


from flask import Flask, request

app = Flask(__name__)


@app.route("/host/")
def get_uptime():
    return f"Current host is:{request.host} "


if __name__ == "__main__":
    port = 5000
    try:
        app.run(debug=True, port=port)
    except OSError as exc:
        pass
        command_str = "lsof -ti :5000"
        command = shlex.split(command_str)
        result = subprocess.run(command, capture_output=True)
        stdout = result.stdout.decode()
        try:
            for pid in stdout.split('\n'):
                os.kill(int(pid), 9)
        except ValueError:
            pass
        resul = subprocess.run(["python", "task_2.py"])
        print(resul.stdout)




