#!/usr/bin/python3
import flask

"""
a script that starts a Flask web application
"""
app = flask (__name__)

@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def text():
    return "C text"

if __name == ' __main__':
    app.run(host='0.0.0.0', port=5000)
