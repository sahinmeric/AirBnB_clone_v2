#!/usr/bin/python3
"""
Module that starts flask web app
"""
from email.policy import strict
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """greeting"""
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
    