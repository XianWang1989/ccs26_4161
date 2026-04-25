
def get_setting():
    settings_sources = [foo(), bar(), baz()]
    return next((setting for setting in settings_sources if setting), default_value)

# Example usage
default_value = 'generic_screen_type'
result = get_setting()
