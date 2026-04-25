
import os
from flask import Flask, g
import sqlite3

# Configure
DATABASE = os.path.expanduser('~/Dropbox/coding/webapp2/tmp/test.db')  # Update this line
DEBUG = True
SECRET_KEY = 'development key'

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

# Ensure your app structure correctly includes routes and the main block
if __name__ == '__main__':
    app.run(debug=DEBUG)
