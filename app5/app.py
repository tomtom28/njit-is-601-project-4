from flask import Flask


app = Flask(__name__)


# TODO
# https://hackersandslackers.com/configure-flask-applications
# What Not To Do: Inline Configuration


@app.route("/")
def home():
    return "Basic Setup Done!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True)