#!/usr/bin/python3
"""Module starts a Flask web application"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """Greet the user"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """Shows HBNB"""
    return "HBNB"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
