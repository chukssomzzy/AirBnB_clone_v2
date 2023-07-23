#!/usr/bin/python3
""" Connect to storage and list all states"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Render a state template"""
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown(fnc):
    """Remove the session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
