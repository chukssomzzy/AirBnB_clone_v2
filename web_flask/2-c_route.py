#!/usr/bin/python3
"""starts a flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """Defines the index route"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Defines the hbnb route"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """displays text from url"""
    if (text):
        text = text.replace("_", " ")
    return f"C {text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
