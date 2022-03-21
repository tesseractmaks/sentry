"""
Ещё раз повторите вызовы через Postman к endpoint, которые мы разбирали на уроках.
"""
import json

from flask import Flask, request

app = Flask(__name__)


@app.route("/sum/", methods=["POST"])
def sum_json():
    form_data = request.get_data(as_text=True)
    data_object = json.loads(form_data)
    result_str = ",".join(
        str(a1 + a2) for a1, a2 in zip(data_object["array1"], data_object["array2"])
    )
    return f"Your result is [{result_str}]"


if __name__ == "__main__":
    app.run(debug=True)