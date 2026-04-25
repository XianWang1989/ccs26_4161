
def get_preferred_setting():
    # Define your functions that return settings
    def foo():
        # Ideally, this will retrieve user-specific settings
        return None  # Placeholder

    def bar():
        # This retrieves account-wide settings
        return None  # Placeholder

    def baz():
        # This retrieves system-wide defaults
        return "default_setting"  # Placeholder for illustration

    # Create a list of functions to call
    check_functions = [foo, bar, baz]

    # Use next to find the first non-None result
    return next((func() for func in check_functions if func() is not None), None)

# Example use
preferred_setting = get_preferred_setting()
print(preferred_setting)
