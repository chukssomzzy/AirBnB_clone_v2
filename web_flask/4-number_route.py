#!/usr/bin/python3
"""starts a flask web application

Routes:
    /: display "Hello HBNB"
    /hbnb: displays "HBNB"
    /c/<text>: displays "C", followed by the value of the text variable
    (replace underscore_ symbol with a space)
    /python/(<text>): display "python", followed by the value fo the text
    variable
    /number/<n>: display "n is a number" only if n is an integer
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """Defines the index route"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def index_hbnb():
    """Defines the hbnb route"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """Displays url params"""
    if (text):
        text = text.replace("_", " ")
    return f"C {text}"


@app.route("/python/", defaults={"text": "is cool"},
           strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_cool(text):
    """displays 'Python'. followed by the value of text"""
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route("/number/<int:n>", strict_slashes=False)
def display_number(n):
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
