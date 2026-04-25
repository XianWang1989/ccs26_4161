
def get_user_setting():
    # Define your functions that can return values
    def foo():
        # Retrieve user-specific setting, return None if not set
        return None  # Example

    def bar():
        # Retrieve account-wide setting, return None if not set
        return "account-wide-setting"  # Example

    def baz():
        # Retrieve system-wide setting, return None if not set
        return "system-wide-setting"  # Example

    # List of functions in priority order
    settings_checks = (foo, bar, baz)

    # Retrieve the first non-falsy result
    return next((check() for check in settings_checks if check()), None)

# Example usage
result = get_user_setting()
print(result)  # This would print 'account-wide-setting' in this case
