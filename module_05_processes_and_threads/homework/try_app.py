import os
import shlex
import subprocess

from flask import Flask

app_try = Flask('test2')


@app_try.route('/test2')
def _test2():
    return 'Im Working'


def run_app(port):
    while True:
        try:
            app_try.run(port=port)
        except OSError:
            command_str = shlex.split(f'lsof -i :{port}')
            result = subprocess.run(command_str, capture_output=True)
            output = result.stdout.decode().split('\n')
            for line in output:
                if line.startswith('python'):
                    line = line.split()
                    pid = int(line[1])
                    os.kill(pid, 9)


if __name__ == '__main__':
    test_port = 5000
    run_app(test_port)
