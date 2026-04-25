
def get_user_setting():
    return next((x for x in (foo(), bar(), baz()) if x), default_value)
