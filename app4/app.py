from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return "Hello World!"


@app.route("/api/v1/users/", methods=['GET', 'POST', 'PUT'])
def users():
    # ... Logic goes here
    return "This API endpoint accepts GET, POST, or PUT requests"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
