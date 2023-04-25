#!/usr/bin/env python3
""" Script of a flask framework project """

from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union, Dict


class Config:
    """ config class for flask app """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """ Returns user dictionary if any """
    login_id = request.args['login_as']
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request() -> None:
    """ Finds user and set as global """
    g.user = get_user()


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
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
