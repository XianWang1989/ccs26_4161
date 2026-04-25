
def get_setting():
    return next(
        (value for value in (foo(), bar(), baz()) if value), 
        None  # Default value if all checks fail
    )
