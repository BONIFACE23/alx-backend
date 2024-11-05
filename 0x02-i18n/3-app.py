#!/usr/bin/env python3
""" A basic Flask app """
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


class Config(object):
    """ an object to configure the new application """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """determine the best match with our supported languages."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


# babel = Babel(app, locale_selector=get_locale)
@app.route('/', strict_slashes=False)
def index() -> str:
    """main route for our app"""
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run()
