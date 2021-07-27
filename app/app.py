from flask import Flask, Markup
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


@app.route("/logic")
def logic():
    value = square_of_number_plus_nine(5)
    return str(value)


@app.route("/")
def hello():
    return Markup("<h1>Hello World!</h1>")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
