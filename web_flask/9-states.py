#!/usr/bin/python3
# script that start flask
from flask import Flask, render_template
from models import storage
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
    return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_python(text="is cool"):
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


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even_number(n):
    """function that print <integer> is a number"""
    if n % 2 == 0:
        msj = "{} is even".format(n)
        return render_template('6-number_odd_or_even.html', msj=msj)
    msj = "{} is odd".format(n)
    return render_template('6-number_odd_or_even.html', msj=msj)


@app.teardown_appcontext
def remove_session(exc):
    """Remove session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def list_states():
    """list all states"""
    data = storage.all("State")
    return render_template('7-states_list.html', data=data)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """list all cities by state"""
    data = []
    data.append(storage.all("State"))
    data.append(storage.all("City"))
    return render_template('8-cities_by_states.html', data=data)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def list_states_by_id(id=None):
    """list all states or one by id"""
    data = []
    if id is not None:
        for item in storage.all("State").values():
            if item.id == id:
                data.append({"State": item})
                data.append(storage.all("City"))
                return render_template("9-states.html", data=data)
        return render_template('9-states.html', data=None)

    data.append(storage.all("State"))
    return render_template('9-states.html', data=data)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
