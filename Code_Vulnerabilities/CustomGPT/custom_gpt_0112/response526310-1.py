
def get_screen_type():
    checks = (foo, bar, baz)  # Functions to check in order
    return next((check() for check in checks if check()), None)

# Usage
screen_type = get_screen_type()
