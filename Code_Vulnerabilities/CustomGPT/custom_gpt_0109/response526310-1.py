
def get_user_setting():
    # Define your functions that retrieve settings
    def foo():
        # Logic to get user-specific setting
        return None  # Placeholder

    def bar():
        # Logic to get account-wide setting
        return 'account_setting'  # Example value

    def baz():
        # Logic to get system-wide default setting
        return 'default_setting'  # Example value

    # List of functions to check in order of priority
    settings_functions = [foo, bar, baz]

    # Use next() with a generator expression to return the first truthy value
    return next((func() for func in settings_functions if func()), None)

# Example usage
setting = get_user_setting()
print(setting)  # Prints 'account_setting' based on the placeholder logic
