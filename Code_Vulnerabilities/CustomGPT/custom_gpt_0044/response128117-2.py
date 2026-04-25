
from __future__ import with_statement
from contextlib import closing
from flask import Flask, render_template, request, session, g, redirect, url_for, abort, flash
import sqlite3
import os

# config
DATABASE = '~/home/aaron/Dropbox/coding/webapp2/tmp/test.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    database_path = os.path.expanduser(app.config['DATABASE'])  # Expand ~ to full path
    return sqlite3.connect(database_path)

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()

# Add your route definitions here
# @app.route('/')
# def index():
#     return render_template('index.html')

if __name__ == '__main__':
    app.run()
