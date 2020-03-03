from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return "Method Used: %s" % request.method


@app.route('/beacon', methods=['GET', 'POST'])
def beacon():
    if request.method == 'POST':
        return "YOU ARE USING POST"
    else:
        return "YOUR ARE PROBABLY USSING GET"


if __name__ == "__main__":
    app.run(debug=True)
