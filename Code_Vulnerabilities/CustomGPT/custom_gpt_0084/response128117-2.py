
def connect_db():
    return sqlite3.connect(os.path.expanduser(app.config['DATABASE']))
