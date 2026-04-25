
def get_setting():
    return next(
        (var for var in (foo(), bar(), baz(), ...) if var),  # Add more functions as needed
        None
    )
