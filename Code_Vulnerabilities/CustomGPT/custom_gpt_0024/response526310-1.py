
def get_setting():
    # Define a list of functions to check for the setting
    options = [foo, bar, baz]

    # Use next to find the first non-falsy result
    return next((option() for option in options if option()), None)

# Usage
setting = get_setting()
