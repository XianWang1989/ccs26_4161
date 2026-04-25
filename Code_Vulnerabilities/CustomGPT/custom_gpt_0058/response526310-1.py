
def get_user_setting():
    # Define functions simulating the user's settings retrieval process
    def foo():
        # Placeholder for user-specific setting
        return None  # Simulating no value

    def bar():
        # Placeholder for account-wide setting
        return None  # Simulating no value

    def baz():
        # Placeholder for system-wide generic setting
        return "default_setting"  # Simulating a default value

    # List of functions in order of priority
    checks = [foo, bar, baz]

    for check in checks:
        result = check()
        if result:
            return result  # Return the first truthy value

    return None  # In case all functions return falsy values

# Usage
screen_setting = get_user_setting()
print(screen_setting)  # This will print 'default_setting'
