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
    /number_template/<n>: display a HTML page only if n is an integer
"""
from flask import Flask, render_template

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


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Render the the number.html page"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
