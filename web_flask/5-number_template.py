#!/usr/bin/python3
# script that start flask
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """function that print Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """function that print HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_something(text):
    """function that print c <something>"""
    return "c {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_something(text="is cool"):
    """function that print python <something>"""
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def n_is_number(n):
    """function that print <integer> is a number"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def template_number(n):
    """function that print <integer> is a number"""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
