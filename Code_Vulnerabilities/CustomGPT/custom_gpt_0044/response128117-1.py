
import os

def connect_db():
    database_path = os.path.expanduser(app.config['DATABASE'])
    return sqlite3.connect(database_path)
