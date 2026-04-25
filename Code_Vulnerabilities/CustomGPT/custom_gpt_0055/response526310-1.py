
def get_setting():
    functions = [foo, bar, baz]  # List of functions to check
    # Iterate through each function and return the first truthy value
    return next((func() for func in functions if func()), None)

# Usage
setting = get_setting()
