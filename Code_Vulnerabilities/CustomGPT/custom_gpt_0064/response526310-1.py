
def get_setting():
    return next(
        (setting for setting in (foo(), bar(), baz()) if setting),
        default_value  # Specify a default value if all checks fail
    )
