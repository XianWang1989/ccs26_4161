
def get_user_setting():
    return next((var for var in (foo(), bar(), baz()) if var), None)
