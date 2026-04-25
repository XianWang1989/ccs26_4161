
from __future__ import with_statement
from contextlib import closing
from flask import Flask, render_template, request, session, g, redirect, url_for, abort, flash
import sqlite3
import os

# Config
DATABASE = os.path.expanduser('~/Dropbox/coding/webapp2/tmp/test.db')
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    """Connects to the specific database."""
    return sqlite3.connect(app.config['DATABASE'])

@app.before_request
def before_request():
    """Creates a database connection before serving requests."""
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    """Closes the database connection at the end of the request."""
    if hasattr(g, 'db'):
        g.db.close()

# Define your routes here

if __name__ == '__main__':
    app.run()
