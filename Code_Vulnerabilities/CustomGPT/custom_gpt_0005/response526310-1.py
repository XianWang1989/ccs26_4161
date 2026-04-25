
def get_user_setting():
    settings = (foo, bar, baz)  # List of functions to check

    # Return the first truthy result from the functions
    return next((setting() for setting in settings if setting()), None)

result = get_user_setting()
