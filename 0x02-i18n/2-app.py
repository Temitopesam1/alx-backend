#!/usr/bin/env python3
""" Script of a flask framework project """

from flask import Flask, render_template
from flask_babel import Babel
from flask import request

app = Flask(__name__)
babel = Babel(app)


class Config:
    """ config class for flask app """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


@babel.localeselector
def get_locale() -> str:
    """ function to get locale """
    return request.accept_languages.best_match(Config['LANGUAGES'])


@app.route("/", strict_slashes=False)
def hello() -> str:
    """ A function to return HTML template """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
