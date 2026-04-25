
def get_screen_type():
    return next(
        (var for var in (foo(), bar(), baz()) if var),
        None  # or any default value you prefer
    )
