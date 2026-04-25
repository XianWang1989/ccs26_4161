
def get_setting():
    settings = (foo(), bar(), baz())

    # Use next with a generator expression to find the first truthy value
    return next((setting for setting in settings if setting), None)

# Example usage
result = get_setting()
