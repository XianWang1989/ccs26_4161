
def get_setting():
    # Assume these functions return either a value or None
    settings_checks = [foo, bar, baz]  # List of functions to check

    # Using a generator expression with next() to return the first non-None result
    return next((check() for check in settings_checks if check()), "default_setting")

# Example usage
result = get_setting()
print(result)
