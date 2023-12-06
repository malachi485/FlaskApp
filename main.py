from flask import Flask

app = Flask(__name__)


@app.route('/')
def genius():
	return '<h1>Hello, Genius</h1>'
