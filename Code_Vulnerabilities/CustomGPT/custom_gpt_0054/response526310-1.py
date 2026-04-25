
def get_setting():
    return next(
        (var for var in (foo(), bar(), baz()) if var),
        None  # Default value if all checks return None or evaluate to False
    )
