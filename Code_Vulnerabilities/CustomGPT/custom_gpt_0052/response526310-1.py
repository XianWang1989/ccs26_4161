
def get_setting():
    settings_sources = (foo(), bar(), baz())

    # Using next to get the first truthy value
    return next((setting for setting in settings_sources if setting), None)

# Example usage:
result = get_setting()
