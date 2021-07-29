from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return "Hello World!"


@app.route("/api/v1/users/", methods=['GET', 'POST', 'PUT'])
def users():
    # ... Logic goes here
    return "This API endpoint accepts GET, POST, or PUT requests"


@app.route('/user/<username>')
def profile(username):
    # ... Logic goes here
    return "Hello, " + str(username)


@app.route('/<int:year>/<int:month>/<title>')
def article(year, month, title):
    # ... Logic goes here
    return "Article Title: " + str(title) + "<br/> Month: " + str(month) + "<br/> Year: " + str(year)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
