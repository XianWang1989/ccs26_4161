
def get_user_setting():
    return next(
        (var for var in (foo(), bar(), baz()) if var),
        None  # Default value if none of the checks return a truthy value
    )

result = get_user_setting()
if result is not None:
    return result
