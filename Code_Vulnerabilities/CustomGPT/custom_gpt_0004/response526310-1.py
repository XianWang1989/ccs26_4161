
def get_setting():
    # Define the functions to check
    functions = [foo, bar, baz]

    # Use next() with a generator expression to find the first truthy value
    return next((func() for func in functions if func()), None)

# Call the function to retrieve the setting
result = get_setting()
