#!/usr/bin/env python3
""" Script of a flask framework project """

from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """ config class for flask app """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCAL = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route("/", strict_slashes=False)
def hello() -> str:
    """ A function to return HTML template """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
