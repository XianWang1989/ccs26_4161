
import os

# Update the DATABASE path
DATABASE = os.path.expanduser('/home/aaron/Dropbox/coding/webapp2/tmp/test.db')

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])  # This will now use the correct expanded path
