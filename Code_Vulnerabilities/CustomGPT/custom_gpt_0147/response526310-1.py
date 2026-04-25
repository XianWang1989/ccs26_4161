
def get_user_screen_type():
    # List of functions to check the screen type in order of priority
    check_functions = [foo, bar, baz]

    # Iterate through the list and return the first non-falsy value
    return next((func() for func in check_functions if func()), "default_screen_type")
