#!/usr/bin/python3
"""starts a flask web application

Routes:
    /: display "Hello HBNB"
    /hbnb: displays "HBNB"
    /c/<text>: displays "C", followed by the value of the text variable
    (replace underscore_ symbol with a space)
    /python/(<text>): display "python", followed by the value fo the text
    variable
    default: text = "is cool"
"""
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
    """Displays url params"""
    if (text):
        text = text.replace("_", " ")
    return f"C {text}"


@app.route("/python/", defaults={"text": "is cool"},
           strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """displays 'Python'. followed by the value of text"""
    text = text.replace("_", " ")
    return f"Python {text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
