
def get_setting():
    # Define your functions that might return a setting
    def foo():
        # Simulate getting user-specific screen type
        return None  # Suppose there's no user-specific type

    def bar():
        # Simulate getting account-wide screen type
        return "account-wide setting"  # This one has a value

    def baz():
        # Simulate getting system-wide generic screen type
        return "default setting"  # This one has a value

    # Create a list of functions in priority order
    checks = [foo, bar, baz]

    # Use next() with a generator expression to return the first truthy result
    return next((check() for check in checks if check()), None)

# Example usage
chosen_setting = get_setting()
print(chosen_setting)  # Output: account-wide setting
