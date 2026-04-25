
def get_setting():
    return next((setting for setting in (foo(), bar(), baz()) if setting), default_value)

# Usage
setting_value = get_setting()
