
def get_setting():
    return next(
        (setting for setting in (foo(), bar(), baz()) if setting),
        None
    )
