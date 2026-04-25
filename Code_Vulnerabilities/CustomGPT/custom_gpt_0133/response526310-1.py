
def get_screen_type():
    # Define a list of functions to check in order of priority
    checks = [foo, bar, baz]

    # Use next() to find the first value that returns a truthy result
    return next((func() for func in checks if func()), None)

# Example usage
screen_type = get_screen_type()
