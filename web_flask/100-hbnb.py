#!/usr/bin/python3
"""Application Server """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exc=None):
    """Close session and obtain a new one"""
    storage.close()


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Create route for /hbnb"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    return render_template("100-hbnb.html", states=states, amenities=amenities,
                           places=places)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
