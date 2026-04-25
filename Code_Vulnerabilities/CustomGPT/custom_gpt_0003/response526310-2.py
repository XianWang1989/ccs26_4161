
def get_user_setting():
    settings = [
        foo(), bar(), baz(), # Add more functions as needed
        # more functions up to 100+
    ]
    return next((setting for setting in settings if setting), None)
