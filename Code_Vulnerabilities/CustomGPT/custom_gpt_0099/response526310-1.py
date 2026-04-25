
def get_setting():
    settings_sources = [foo, bar, baz]
    return next((setting() for setting in settings_sources if setting()), default=None)
