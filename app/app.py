from flask import Flask
from logic import square_of_number_plus_nine


# Create Flask's `app` object
app = Flask(__name__)


# Create Flask's `app` object
app = Flask(
    __name__,
    instance_relative_config=False,
    template_folder="templates",
    static_folder="static"
)


@app.route("/")
def hello():
    value = square_of_number_plus_nine(5)
    return str(value)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
