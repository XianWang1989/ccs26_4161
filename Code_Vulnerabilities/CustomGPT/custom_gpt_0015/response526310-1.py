
def get_screen_type():
    return next(
        (value for value in (foo(), bar(), baz()) if value),
        None  # Default value if all checks fail
    )

# Usage
screen_type = get_screen_type()
