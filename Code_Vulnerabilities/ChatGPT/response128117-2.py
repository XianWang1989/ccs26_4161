
if not os.path.exists(DATABASE):
    raise Exception("The database file does not exist at the specified path: {}".format(DATABASE))
