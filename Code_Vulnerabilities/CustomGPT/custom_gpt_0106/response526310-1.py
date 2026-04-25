
def get_setting():
    settings = (foo(), bar(), baz())  # List of functions to call
    return next((setting for setting in settings if setting), default_value)

# Example scenario, replace `default_value` with a suitable fallback
default_value = "generic_screen_type"
result = get_setting()
