#!/usr/bin/env python3
""" Script of a flask framework project """

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """ config class for flask app """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ function to get locale """
    locale = request.args['locale']
    if locale and (locale in Config.LANGUAGES):
        return locale
    return request.accept_languages.best_match(Config['LANGUAGES'])


@app.route("/", strict_slashes=False)
def hello():
    """ A function to return HTML template """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
