#!/usr/bin/python3
"""starts a flask web application
Routes:
    /: display "Hello HBNB!"
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """Defines the index route"""
    return "Hello HBNB!"
