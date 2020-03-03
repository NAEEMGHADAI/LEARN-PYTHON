from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    name = "NAEEM"
    return render_template('index.html', id=name)


@app.route('/names/<id>')
def name(id):
    names = ['naeem', 'AbdulKadir', 'Ahmed']
    id = int(id)
    if id > len(names):
        return "NO DATA FOUND"
    return render_template('names.html', name=names[int(id)], id=id)


app.run(debug=True)
