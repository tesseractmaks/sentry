from flask import Flask, jsonify, make_response, render_template

app = Flask(__name__)


@app.route('/hello')
@app.route('/hello/<username>')
def hello_world(username='username'):
    return make_response(jsonify(message='hello', name=username))


app.add_url_rule('/photos/<path:filename>', endpoint='photos', view_func=app.send_static_file)


@app.route('/<path:filename>')
def serve_static(filename):
    return render_template('index.html', image=filename)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False, port=80)


