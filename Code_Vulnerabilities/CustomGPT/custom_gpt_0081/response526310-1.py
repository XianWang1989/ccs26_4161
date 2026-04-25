
def get_user_setting():
    # Simulating the functions that retrieve user settings
    def foo():
        return None  # User specific screen type (None means no specific setting)

    def bar():
        return "account-wide-type"  # User account-wide screen type

    def baz():
        return "system-wide-generic-type"  # Default system-wide screen type

    # Use a generator expression to evaluate functions in order
    return next((func() for func in (foo, bar, baz) if func()), "default-type")

# Usage
screen_type = get_user_setting()
print(screen_type)  # Output will be "account-wide-type" or "system-wide-generic-type" or "default-type"
