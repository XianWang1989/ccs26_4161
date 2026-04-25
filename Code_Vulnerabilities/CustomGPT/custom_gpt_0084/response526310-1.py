
def get_user_setting():
    settings = [foo, bar, baz]  # List of functions to check

    for setting_func in settings:
        var = setting_func()
        if var:
            return var

    return None  # Or a default value if all checks fail
