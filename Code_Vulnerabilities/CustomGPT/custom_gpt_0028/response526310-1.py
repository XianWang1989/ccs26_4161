
def get_user_setting():
    settings_getters = [foo, bar, baz]  # List of functions to call

    # Use next() with a generator expression to find the first truthy value
    return next((setting() for setting in settings_getters if setting()), None)

# Example usage
result = get_user_setting()
