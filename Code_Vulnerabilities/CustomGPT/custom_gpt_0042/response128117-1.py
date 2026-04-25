
import os
from flask import Flask, g
import sqlite3

# Config
DATABASE = os.path.expanduser('~/home/aaron/Dropbox/coding/webapp2/tmp/test.db')
DEBUG = True
SECRET_KEY = 'development key'

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    """Connects to the specific database."""
    return sqlite3.connect(app.config['DATABASE'])

@app.before_request
def before_request():
    """Make sure the database is connected before each request."""
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    """Close the database connection at the end of the request."""
    if hasattr(g, 'db'):
        g.db.close()

# Start of the application
if __name__ == '__main__':
    app.run(debug=DEBUG)
