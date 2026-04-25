
import os
import sqlite3
from flask import Flask, g

# config
DATABASE = os.path.expanduser('~/home/aaron/Dropbox/coding/webapp2/tmp/test.db')
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])  # This line will work now

@app.before_request
def before_request():
    g.db = connect_db()  # This line will also work now

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()

# Ensure to add your app routes and run the app below
if __name__ == '__main__':
    app.run(debug=True)
