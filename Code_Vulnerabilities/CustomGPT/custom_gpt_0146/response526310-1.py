
def get_screen_type():
    return next(
        (var for var in (foo(), bar(), baz()) if var),
        None  # Default value if all are falsy
    )
