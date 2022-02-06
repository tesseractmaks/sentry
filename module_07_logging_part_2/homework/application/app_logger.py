import shlex, subprocess
from typing import Optional
from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import InputRequired

# from probe import published

app = Flask(__name__)


class WorkerForm(FlaskForm):
   x = IntegerField(validators=[InputRequired()])


@app.route("/logs", methods=["POST"])
def publish():
    form = WorkerForm()
    x = form.x.data
    res = published(x)
    # print(res)
    return res


if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False

    app.run(debug=True)
    # published()


