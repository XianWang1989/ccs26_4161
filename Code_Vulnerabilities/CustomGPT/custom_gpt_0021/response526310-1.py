
def get_setting():
    settings = [foo(), bar(), baz()]
    return next((s for s in settings if s), None)

# Example usage
result = get_setting()
