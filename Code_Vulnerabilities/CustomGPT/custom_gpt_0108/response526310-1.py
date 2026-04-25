
def get_preferred_setting():
    # Define a list of functions to check
    functions = [foo, bar, baz]

    # Use next with a generator expression to return the first truthy value
    return next((func() for func in functions if func()), None)
