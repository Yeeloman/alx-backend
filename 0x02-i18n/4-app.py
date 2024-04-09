#!/usr/bin/env python3
"""3. Parametrize templates"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """config class for flask"""
    """initiate config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """determine the best
    match with the
    supported languages"""
    local = request.args.get('locale')
    if local in app.config['LANGUAGES']:
        return local
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/',  strict_slashes=False)
def index():
    """serving the template"""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run()
