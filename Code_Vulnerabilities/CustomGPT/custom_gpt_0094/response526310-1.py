
def get_user_setting():
    # Example functions returning settings
    def foo(): return None  # User-specific setting
    def bar(): return "account-wide"  # Account-wide setting
    def baz(): return "generic"  # Generic setting

    # List of functions to check
    settings_check = (foo, bar, baz)

    # Use next with a generator to get the first truthy value
    return next((setting() for setting in settings_check if setting()), "default_value")

# Usage
result = get_user_setting()
print(result)  # Outputs: "account-wide" or "generic" or "default_value"
