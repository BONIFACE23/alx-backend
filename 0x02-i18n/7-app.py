#!/usr/bin/env python3
""" A basic Flask app """
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Dict, Union
import pytz

app = Flask(__name__)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """ an object to configure the new application """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


def get_user(id: Union[str, None]) -> Union[Dict, None]:
    """find a user if any"""
    return users.get(int(id), 0)


@app.before_request
def before_request():
    """a user login system"""
    setattr(g, 'user', get_user(request.args.get('login_as', 0)))


@babel.timezoneselector
def get_timezone() -> str:
    """
    Gets timezone from request object
    """
    tz = request.args.get('timezone', '').strip()
    if not tz and g.user:
        tz = g.user['timezone']
    try:
        return pytz.timezone(tz).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']


@babel.localeselector
def get_locale() -> str:
    """determine the best match with our supported languages."""
    locale = request.args.get('locale')
    if locale in Config.LANGUAGES:
        return locale
    if g.user and g.user["locale"] in Config.LANGUAGES:
        return g.user["locale"]
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """main route for our app"""
    return render_template("7-index.html")


if __name__ == "__main__":
    app.run()
