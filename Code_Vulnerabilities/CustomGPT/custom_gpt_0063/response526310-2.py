
def get_setting():
    settings_funcs = [foo, bar, baz, ...]  # Add your other functions here
    return next((func() for func in settings_funcs if func()), None)
