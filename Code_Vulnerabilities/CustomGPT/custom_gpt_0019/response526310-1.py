
def get_user_setting():
    settings = [foo, bar, baz]  # List of functions to check
    return next((func() for func in settings if func()), None)

# Usage
result = get_user_setting()
