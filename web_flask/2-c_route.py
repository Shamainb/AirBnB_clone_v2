#!/usr/bin/python3
from flask import flask

"""
a script that starts a Flask web application
"""
app = flask (__name__)

@app.route("/", strict_slashes=False)
def hello():
    return <p> Hello HBNB! </p>

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return <p> HBNB </p>

@app.route("/c/<text>", strict_slashes=False)
def text():
    return <p> C </p> <p> text </p>

if __name == ' __main__':
    app.run(host='0.0.0.0', port=5000)
