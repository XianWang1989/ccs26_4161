
import os
from flask import Flask, g
import sqlite3

# Config
DATABASE = os.path.expanduser('~/home/aaron/Dropbox/coding/webapp2/tmp/test.db')
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    """Connect to the specific database."""
    return sqlite3.connect(app.config['DATABASE'])

@app.before_request
def before_request():
    """Open a new database connection before each request."""
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    """Close the database connection after each request."""
    if hasattr(g, 'db'):
        g.db.close()

# Additional Flask code would go here (routes, etc.)

if __name__ == '__main__':
    app.run(debug=DEBUG)
