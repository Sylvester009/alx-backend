#!/usr/bin/env python3
from flask import Flask, page_template

app = Flask(__name__)


@app.route('/')
def index():
    return page_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
