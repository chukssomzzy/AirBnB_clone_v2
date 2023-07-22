#!/usr/bin/python3
""" Connect to storage and list all states"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def state_list():
    """Render a state template"""
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(fnc):
    """Remove the session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
