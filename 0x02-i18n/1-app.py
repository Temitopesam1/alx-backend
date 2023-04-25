#!/usr/bin/python3
""" Script of a flask framework project """

from flask import Flask, render_template
from flask_babel import Babel
from flask import request


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ config class for flask app """
    LANGUAGES = ['en', 'fr']


@babel.localeselector
def get_locale():
    """ function to get locale """
    return request.accept_languages.best_match(Config['LANGUAGES'])


@app.route("/", strict_slashes=False)
def hello():
    """ A function to return HTML template """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
