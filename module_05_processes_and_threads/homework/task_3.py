import contextlib
import os
import re
import shlex, subprocess

from flask import Flask, request




class SavedFile:

    def __init__(self, debug, app, port):
        self.debug = debug
        self.port = port
        self.app = app

    def __enter__(self):
        app = self.app.run(debug=self.debug, port=self.port)
        return app



    def __exit__(self, type, value, traceback):
        print(value)
        return True

class saved_file:
    def __init__(self, stdout):
        self.stdout = stdout

    def __enter__(self):
        return self.stdout

    def __exit__(self, type, value, traceback):
        [os.kill(int(pid), 9) for pid in self.stdout.split('\n')]
        return True


if __name__ == '__main__':
    app = Flask(__name__)

    @app.route("/host/")
    def get_uptime():
        return f"Current host is:{request.host} "

    port = 5000

    with SavedFile(debug=True, app=app, port=port) as app_run:
        app_run(debug=True, port=port)
        command_str = "lsof -ti :5000"
        command = shlex.split(command_str)
        result = subprocess.run(command, capture_output=True)
        stdout = result.stdout.decode()
        with saved_file(stdout=stdout):
            subprocess.run(["python", "task_3.py"])



        # try:
        #     for pid in stdout.split('\n'):
        #         os.kill(int(pid), 9)
        # except ValueError:
        #
        #     resul = subprocess.run(["python", "task_3.py"])
        #     print(resul.stdout)





        # [os.kill(int(pid), 9) for pid in stdout.split('\n')]

        # subprocess.run(["python", "task_3.py"])

    # print(stdout, '--')





        #
        #     print('----------------------------------------')

            # resul = subprocess.run(["python", "task_3.py"])
            # print(resul.stdout)
            # print(f)




