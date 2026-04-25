
def get_setting():
    settings_sources = [foo, bar, baz]  # List of functions to check

    for setting_function in settings_sources:
        result = setting_function()
        if result:
            return result

    return None  # Return None if no setting is found
