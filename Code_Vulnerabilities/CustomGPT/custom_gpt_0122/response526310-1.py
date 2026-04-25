
def get_user_setting():
    def foo():
        # logic for user-specific setting
        return None

    def bar():
        # logic for account-wide setting
        return None

    def baz():
        # logic for system-wide generic setting
        return "default_setting"

    # List of functions to check in order of priority
    checks = [foo, bar, baz]

    for check in checks:
        result = check()
        if result is not None:
            return result

    return None  # Default return if no settings found

# Example usage
setting = get_user_setting()
print(setting)
