
import os
from __future__ import with_statement
from contextlib import closing
from flask import Flask, render_template, request, session, g, redirect, url_for, abort, flash
import sqlite3

# Config
DATABASE = os.path.expanduser('~/home/aaron/Dropbox/coding/webapp2/tmp/test.db') # Use os.path.expanduser
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE']) # LINE 17

@app.before_request
def before_request():
    g.db = connect_db() # LINE 22

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()

# Optional: Define a route to test database connection
@app.route('/')
def index():
    # Example query to check if the database connection works
    cur = g.db.execute('SELECT * FROM some_table') # Modify according to your table
    entries = cur.fetchall()
    return render_template('index.html', entries=entries)

if __name__ == '__main__':
    app.run(debug=True)
