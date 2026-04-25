
def get_screen_type():
    # Define your functions that return the desired values
    def foo():
        # Logic to get user-specific setting
        ...

    def bar():
        # Logic to get account-wide setting
        ...

    def baz():
        # Logic to get system-wide setting
        ...

    # List of functions to check in order of priority
    checks = [foo, bar, baz]

    # Iterate over the functions and return the first non-None result
    for check in checks:
        var = check()
        if var:
            return var

    # Return a default value if none of the checks succeed
    return None  # or any appropriate default value
