#!/usr/bin/env python3
""" A Basic Flask App"""

from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    """Render the index template."""
    return render_template('0-index.html')


while __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
