
def get_user_setting():
    # Define the functions you want to check in order of priority
    checks = [foo, bar, baz]

    # Use next to find the first non-falsy result
    return next((check() for check in checks if check()), "default_value")
