
def get_screen_type():
    return next(
        (setting for setting in (foo(), bar(), baz()) if setting),
        None  # default value if all are None or false
    )
