
from __future__ import with_statement
from contextlib import closing
from flask import Flask, render_template, request, session, g, redirect, url_for, abort, flash
import sqlite3
import os

#config
DATABASE = os.path.expanduser('~/Dropbox/coding/webapp2/tmp/test.db')
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])  # This will now work correctly

@app.before_request
def before_request():
    g.db = connect_db()  # Attempt to connect to the database

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()

# Your app.route functions would come here
