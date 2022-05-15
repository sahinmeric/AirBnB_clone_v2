#!/usr/bin/python3
"""Module starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_state():
    """Displays a list of states in a website"""
    state_list = storage.all(State).values()
    return render_template('7-states_list.html', state_list=state_list)


@app.teardown_appcontext
def close_storage(db):
    """Closes the current SQLAlchemy session"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
