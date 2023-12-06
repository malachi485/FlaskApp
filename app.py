from flask import Flask

app = Flask(__name__)


@app.route('/')
def genius():
	return '<h1>Hello, Genius</h1>'
@app.route('/about/')
def about():
	return '<h3> It Feels Great To Be A Genius!</h3>
