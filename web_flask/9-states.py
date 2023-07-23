#!/usr/bin/python3
"""Render states and cities by id"""
from flask import Flask, abort, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """States Route"""
    states = storage.all(State)
    return render_template("9-states.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """Find states in storage and display cities related to it"""
    states = storage.all(State)
    key = "State" + f".{id}"
    state = states.get(key)
    if not key:
        abort(404)
    return render_template("9-states.html", state=state)


@app.teardown_appcontext
def teardown(f):
    """close session """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
