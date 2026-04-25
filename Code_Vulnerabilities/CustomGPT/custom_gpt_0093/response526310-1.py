
def get_screen_type():
    # Define a list of functions to check for screen type
    check_functions = [foo, bar, baz]

    # Use next with a generator expression to find the first valid result
    return next((func() for func in check_functions if func()), None)

# Example usage
screen_type = get_screen_type()
