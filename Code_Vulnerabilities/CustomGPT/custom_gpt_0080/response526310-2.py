
def get_setting():
    settings = [foo(), bar(), baz(), ...]  # Add more functions here
    return next((var for var in settings if var), None)
