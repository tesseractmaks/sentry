import sentry_sdk
from flask import Flask
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="https://bb856f4acdba4c3d93d4ea0b9eccd2d5@o4505432482316288.ingest.sentry.io/4505566365941760",
    integrations=[
        FlaskIntegration(),
    ],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)


app = Flask(__name__)


@app.route('/debug-sentry')
def trigger_error():
    division_by_zero = 1 / 0

@app.route('/')
def trigger():
    return "5555555555555555"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
