
def get_user_setting():
    def foo():
        # Simulate fetching user-specific setting
        return None  # Example fallback

    def bar():
        # Simulate fetching account-wide setting
        return None  # Example fallback

    def baz():
        # Simulate fetching system-wide setting
        return "default_setting"  # Example fallback

    # List of functions to check in order of priority
    checks = [foo, bar, baz]

    # Iterate through the functions and return the first truthy value
    return next((func() for func in checks if func()), None)

result = get_user_setting()
print(result)  # Output: default_setting
