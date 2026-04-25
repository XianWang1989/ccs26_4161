
def get_setting():
    settings_funcs = [foo, bar, baz]  # List of functions to check

    return next((func() for func in settings_funcs if func()), default=default_value)

# Usage
result = get_setting()
