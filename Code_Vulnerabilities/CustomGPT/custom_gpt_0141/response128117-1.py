
import os
from flask import Flask, g
import sqlite3

# Configuration
DATABASE = os.path.expanduser('~/home/aaron/Dropbox/coding/webapp2/tmp/test.db')
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])  # LINE 17

@app.before_request
def before_request():
    g.db = connect_db()  # LINE 22

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()

# Example route to demonstrate functionality
@app.route('/')
def index():
    return "Welcome to the Flask App!"

if __name__ == '__main__':
    app.run()
