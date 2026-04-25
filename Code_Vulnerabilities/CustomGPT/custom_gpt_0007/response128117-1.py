
import os
import sqlite3

# config
DATABASE = os.path.expanduser('~/home/aaron/Dropbox/coding/webapp2/tmp/test.db')  # Corrected line
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])  # This line remains the same

@app.before_request
def before_request():
    g.db = connect_db()  # This line remains the same

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()
