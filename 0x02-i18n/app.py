#!/usr/bin/env python3
from flask import Flask, render_template, request, g
from flask_babel import Babel, _
import pytz
from pytz.exceptions import UnknownTimeZoneError
from datetime import datetime

# Mock user database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

class Config:
    """App configuration."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

@babel.localeselector
def get_locale():
    """Determine the best match for supported languages."""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@babel.timezoneselector
def get_timezone():
    """Determine the best match for timezones."""
    timezone = request.args.get('timezone')
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except UnknownTimeZoneError:
            pass  # Invalid timezone, fall through to the next check

    if g.user and g.user['timezone']:
        try:
            pytz.timezone(g.user['timezone'])
            return g.user['timezone']
        except UnknownTimeZoneError:
            pass  # Invalid timezone, fall through to the default

    return app.config['BABEL_DEFAULT_TIMEZONE']

@app.before_request
def before_request():
    """Set user information in flask.g before each request."""
    g.user = get_user()

def get_user():
    """Get user by ID."""
    user_id = request.args.get('login_as')
    if user_id and user_id.isdigit():
        return users.get(int(user_id))
    return None

@app.route('/')
def index():
    """Render the home page with localized content."""
    # Get the current time in the selected time zone
    timezone = get_timezone()
    now = datetime.now(pytz.timezone(timezone))
    formatted_time = now.strftime('%b %d, %Y, %I:%M:%S %p')  # Adjust format if needed
    return render_template('7-index.html', current_time=formatted_time)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
