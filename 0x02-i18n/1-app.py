#!/usr/bin/env python3
"""Module that instantiate
the Babel object in your app"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """ class config that stores the
    languages, locality and timezone"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.url_map.strict_slashes = False
babel = Babel(app)


app.config.from_object(Config)


@app.route('/')
def index():
    """Render the index template."""
    return render_template('1-index.html')


while __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
