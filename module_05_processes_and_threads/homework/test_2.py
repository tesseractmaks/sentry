import contextlib
import os
import re
import shlex, subprocess
import time

from flask import Flask, request
from test_1 import app, port


class RunApp:

    def __init__(self, debug, app, port):
        self.debug = debug
        self.port = port
        self.app = app


    # TODO запускаю приложение с параметрами debug=True, port=5000
    def __enter__(self):
        self.app = self.app.run(debug=self.debug, port=self.port)
        return self.app

    # TODO тут не понимаю почему исключение не заходит в метод __exit__
    def __exit__(self, type, value, traceback):
        print(type)
        return True


class KillsPid:
    def __init__(self, stdout):
        self.stdout = stdout

    # TODO тут просто убиваю процессы и запускаю новый. В self.stdout три элемента
    #  два PID и один такое: ''   - как раз причина ошибки .
    def __enter__(self):
        y = re.findall("[\d+]{5}", str(self.stdout))
        _ = [os.kill(int(pid), 9) for pid in y]
        subprocess.run(["python", "task_1.py"])
        return _

    # TODO тут та же ситуация  не понимаю почему исключение не заходит в метод __exit__
    def __exit__(self, type, value, traceback):
        print(value)
        return True




# @contextlib.contextmanager'
# def kills_pid(stdout):
#    try:
#         # _ = [os.kill(int(pid), 9) for pid in stdout.split('\n')]
#         for pid in stdout.split('\n'):
#             os.kill(int(pid), 9)
#         yield
#    finally:
#        subprocess.run(["python", "task_3.py"])


# if __name__ == '__main__':

# port = 5000


with RunApp(debug=True, app=app, port=port) as app_run:
    command_str = "lsof -ti :5000"
    command = shlex.split(command_str)
    result = subprocess.run(command, capture_output=True)
    stdout = result.stdout.decode()
    with KillsPid(stdout=stdout):
        subprocess.run(["python", "task_1.py"])







        # with kills_pid(stdout=stdout):
        #     subprocess.run(["python", "task_3.py"])



        # try:
        #     for pid in stdout.split('\n'):
        #         os.kill(int(pid), 9)
        # except ValueError:
        #
        #     resul = subprocess.run(["python", "task_3.py"])
        #     print(resul.stdout)



# command_str = "lsof -ti :5000"
# command = shlex.split(command_str)
# result = subprocess.run(command, capture_output=True)
# stdout = result.stdout.decode()
# y = re.findall("[\d+]{5}", str(stdout))
# _ = [os.kill(int(pid), 9) for pid in y]
# time.sleep(1)
# try:
#     subprocess.run(["python", "task_1.py"])
# except:
#     print("--")



