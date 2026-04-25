
import os  # Import os module

DATABASE = os.path.expanduser('~/home/aaron/Dropbox/coding/webapp2/tmp/test.db')  # Expand user path

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])  # LINE 17

@app.before_request
def before_request():
    g.db = connect_db()  # LINE 22
