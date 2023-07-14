import json
from wsgiref import simple_server


class Application(object):
    def __call__(self, environ, start_response):
        if environ['PATH_INFO'] == '/hello':
            return self.hello(environ, start_response)
        elif environ['PATH_INFO'] == '/hello/username':
            return self.hello_user(environ, start_response)
        else:
            start_response('404 Not Found', [('Content-type', 'text/html')])
            return [b'404 Not Found']

    def hello(self, environ, start_response):
        start_response('200 OK', [('Content-type', 'application/json')])
        json_data = json.dumps([{'message': 'Hello'}]).encode("utf-8")
        return [json_data]

    def hello_user(self, environ, start_response):
        start_response('200 OK', [('Content-type', 'application/json')])
        username = environ['USERNAME']
        json_data = json.dumps([{'message': 'Hello', 'user': username}]).encode("utf-8")
        return [json_data]


app = Application()

httpd = simple_server.WSGIServer(
    ('0.0.0.0', 8001),
    simple_server.WSGIRequestHandler,
)
httpd.set_app(app)
httpd.serve_forever()
