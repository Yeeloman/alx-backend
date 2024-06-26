#!/usr/bin/env python3
"""2. Get locale from request"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """config class for flask"""
    def __init__(self) -> None:
        """initiate config class"""
        self.LANGUAGES = ["en", "fr"]
        self.BABEL_DEFAULT_LOCALE = "en"
        self.BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """determine the best
    match with the
    supported languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """serving the template"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
