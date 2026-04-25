
def get_setting():
    settings = (foo(), bar(), baz())
    return next((setting for setting in settings if setting), None)
