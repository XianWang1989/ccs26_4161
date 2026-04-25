
def get_user_setting():
    settings_checkers = [foo, bar, baz]
    return next((setting() for setting in settings_checkers if setting()), None)

# Example usage
result = get_user_setting()
return result
