
def get_user_setting():
    # Define a list of functions to retrieve values in order of priority
    functions = [foo, bar, baz]

    # Use next with a generator expression to find the first truthy result
    return next((func() for func in functions if func()), None)

# Usage
result = get_user_setting()
