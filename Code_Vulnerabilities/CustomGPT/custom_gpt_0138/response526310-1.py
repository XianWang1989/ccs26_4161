
def get_setting():
    settings_checks = [foo, bar, baz]
    return next((setting() for setting in settings_checks if setting()), None)
