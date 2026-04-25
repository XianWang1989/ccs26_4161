
import os
from __future__ import with_statement
from contextlib import closing
from flask import Flask, g

# Config
DATABASE = os.path.expanduser('~/Dropbox/coding/webapp2/tmp/test.db')
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()

# Ensure your main route and other routes are defined here as needed
if __name__ == '__main__':
    app.run(debug=DEBUG)
