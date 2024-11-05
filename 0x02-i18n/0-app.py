#!/usr/bin/env python3
""" A basic Flask app """
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index() -> str:
    """main route for our app"""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run()
