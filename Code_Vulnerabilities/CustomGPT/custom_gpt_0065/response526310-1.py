
def get_user_setting():
    settings_check = [foo, bar, baz]

    # Use a generator expression with next
    return next((setting() for setting in settings_check if setting()), None)

# Example function definitions
def foo():
    # Retrieve user-specific setting
    return None  # or a valid value

def bar():
    # Retrieve account-wide setting
    return None  # or a valid value

def baz():
    # Retrieve system-wide setting
    return "default_setting"  # or a valid value

result = get_user_setting()
print(result)  # Outputs the first non-None result or None
