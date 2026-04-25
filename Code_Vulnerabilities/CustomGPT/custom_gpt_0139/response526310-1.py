
def get_user_setting():
    return next((result for result in (foo(), bar(), baz()) if result), None)
