
def get_user_setting():
    # Define your functions that retrieve settings
    def foo():
        # Example: get specific screen type
        return None  # Placeholder for actual logic

    def bar():
        # Example: get account-wide screen type
        return None  # Placeholder for actual logic

    def baz():
        # Example: get generic screen type
        return "default_screen_type"  # Placeholder for actual logic

    # List of functions to check in order of priority
    functions = [foo, bar, baz]

    # Use next() to retrieve the first truthy result
    return next((func() for func in functions if func()), None)

# Example usage
setting = get_user_setting()
print(setting)  # Outputs the first available screen type
