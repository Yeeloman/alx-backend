#!/usr/bin/env python3
"""1. Basic Babel setup"""

from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """config class for flask"""
    def __init__(self) -> None:
        """initiate config class"""
        self.LANGUAGES = ["en", "fr"]
        self.BABEL_DEFAULT_LOCALE = "en"
        self.BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def index():
    """serving the template"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
