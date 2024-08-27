#!/usr/bin/env python3
"""A Flask module that get
locale from request"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Get the locale for the webpage based on user preferences."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Render the home/index page."""
    return render_template('2-index.html')


while __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
