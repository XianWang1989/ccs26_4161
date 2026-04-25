
import os
from flask import Flask, g
import sqlite3

# Configuration
DATABASE = os.path.expanduser('~/home/aaron/Dropbox/coding/webapp2/tmp/test.db')
DEBUG = True
SECRET_KEY = 'development key'

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    """Connect to the database with the provided configuration"""
    return sqlite3.connect(app.config['DATABASE'])

@app.before_request
def before_request():
    """Before each request, establish a database connection"""
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    """Close the database connection after each request"""
    if hasattr(g, 'db'):
        g.db.close()

if __name__ == '__main__':
    app.run()
