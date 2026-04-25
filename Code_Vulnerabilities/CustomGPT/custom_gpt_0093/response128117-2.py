
if not os.path.exists(app.config['DATABASE']):
    abort(500, description="Database not found.")
