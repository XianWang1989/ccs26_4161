
def get_setting():
    # Define a list of functions to call
    funcs = [foo, bar, baz]

    # Use next with a generator expression to find the first truthy value
    return next((func() for func in funcs if func()), None)

# Example usage
result = get_setting()
