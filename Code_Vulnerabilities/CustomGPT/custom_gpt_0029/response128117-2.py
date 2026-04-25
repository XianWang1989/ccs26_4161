
if not os.path.exists(app.config['DATABASE']):
    raise RuntimeError("Database file does not exist!")
