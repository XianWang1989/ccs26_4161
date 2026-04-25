
def get_setting():
    settings = (foo(), bar(), baz())
    return next((s for s in settings if s), None)

# Usage
setting = get_setting()
if setting:
    return setting
