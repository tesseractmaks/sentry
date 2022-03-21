from flask import Flask

block_app = Flask(__name__)


@block_app.route('/test1')
def _test1():
    return 'Hello World'


if __name__ == '__main__':
    port = 5000
    block_app.run(port=port)
