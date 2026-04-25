
def get_screen_type():
    checks = [foo, bar, baz]  # List of functions to check
    return next((check() for check in checks if check()), None)
