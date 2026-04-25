
def get_setting():
    # Define your check functions
    def foo():
        # Implementation for user-specific setting
        pass

    def bar():
        # Implementation for account-wide setting
        pass

    def baz():
        # Implementation for system-wide setting
        pass

    # List of functions to check
    checks = [foo, bar, baz]

    # Use next() with a generator expression to return the first truthy value
    return next((check() for check in checks if check()), None)

# Usage
result = get_setting()
