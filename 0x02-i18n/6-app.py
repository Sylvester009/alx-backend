#!/usr/bin/env python3
from flask import Flask, render_template, request, g
from flask_babel import Babel, _

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
    # Check if 'locale' is in the request URL and if it's supported
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    
    # Use the locale from the user's settings if available
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    
    # Fall back to the request's Accept-Language headers
    return request.accept_languages.best_match(app.config['LANGUAGES'])

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
    return render_template('5-index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
