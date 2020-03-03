from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "THIS IS"


@app.route('/naeem')
def naeem():
    return '<h2>naeem is smart</h2>'


@app.route('/profile/<username>')
def profile(username):
    return "<h1>Hey there %s</h1>" % username


@app.route('/post/<int:post_id>')
def showpost(post_id):
    return "<h2>your post id is %s</h1>" % post_id


if __name__ == "__main__":
    app.run(debug=True)
