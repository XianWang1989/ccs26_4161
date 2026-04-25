
def get_setting():
    # Define your checks in order of priority
    checks = [foo, bar, baz]

    # Use a generator to find the first truthy value
    return next((var for func in checks if (var := func())), None)

# Example usage
result = get_setting()
