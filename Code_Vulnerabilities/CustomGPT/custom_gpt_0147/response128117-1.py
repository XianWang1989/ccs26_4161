
from __future__ import with_statement
from contextlib import closing
from flask import Flask, g
import sqlite3
import os

# Config
DATABASE = os.path.expanduser('~/home/aaron/Dropbox/coding/webapp2/tmp/test.db')  # LINE 8
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    """Connect to the database."""
    try:
        return sqlite3.connect(app.config['DATABASE'])  # LINE 17
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return None

@app.before_request
def before_request():
    """Open a new database connection before each request."""
    g.db = connect_db()  # LINE 22

@app.teardown_request
def teardown_request(exception):
    """Close the database connection after each request."""
    if hasattr(g, 'db'):
        g.db.close()

if __name__ == '__main__':
    app.run()
