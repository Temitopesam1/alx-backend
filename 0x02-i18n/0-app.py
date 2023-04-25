#!/usr/bin/python3
""" Script of a flask framework project """

from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ A function to return HTML template  """
    return render_template('5-number.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
