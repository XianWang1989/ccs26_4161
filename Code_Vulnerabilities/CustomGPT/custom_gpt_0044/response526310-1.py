
def get_setting():
    return next(
        (var for var in (foo(), bar(), baz()) if var),
        None  # Default value if all checks are None or falsy
    )
