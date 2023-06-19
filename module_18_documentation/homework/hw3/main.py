import operator
from flask import Flask
from flask_jsonrpc import JSONRPC
from flasgger import APISpec, Swagger
from flask_restx import Resource, Api
from apispec_webframeworks.flask import FlaskPlugin
from apispec.ext.marshmallow import MarshmallowPlugin

app = Flask(__name__)
app.config['SWAGGER'] = {
    'openapi': '3.0.0'
}
api = Api(app)

spec = APISpec(
    title="Calkulator",
    version="1.0.0",
    openapi_version="3.0.0",
    plugins=[
        FlaskPlugin(),
        MarshmallowPlugin(),
    ],
)
jsonrpc = JSONRPC(app, '/api', enable_web_browsable_api=True)


@jsonrpc.method('calc.add')
def add(a: float, b: float) -> float:
    """
    Пример запроса:
     $ curl -i -X POST -H "Content-Type: application/json; indent=4" \
         -d
        '{
            "jsonrpc": "2.0",
            "method": "calc.add",
            "params": {"a": 7.8, "b": 5.3},
            "id": "1"
        }' http://localhost:5000/api
    Пример ответа:
    HTTP/1.1 200 OK
    Server: Werkzeug/2.2.2 Python/3.10.6
    Date: Fri, 09 Dec 2022 19:00:09 GMT
    Content-Type: application/json
    Content-Length: 54
    Connection: close
    {
      "id": "1",
      "jsonrpc": "2.0",
      "result": 13.1
    }
    """
    return operator.add(a, b)


@jsonrpc.method('calc.mul')
def mul(a: float, b: float) -> float:
    return operator.mul(a, b)


@jsonrpc.method('calc.truediv')
def truediv(a: float, b: float) -> float:
    return operator.truediv(a, b)


@jsonrpc.method('calc.sub')
def sub(a: float, b: float) -> float:
    return operator.sub(a, b)


swagger = Swagger(app, template=None, template_file="openapi.yaml")

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
