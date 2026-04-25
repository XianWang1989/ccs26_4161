
def get_user_setting():
    # Imagine these functions return None if no setting is found
    return foo() or bar() or baz()

# Example functions
def foo():
    # Logic to get a user-specific setting
    return None

def bar():
    # Logic to get an account-wide setting
    return None

def baz():
    # Logic to get a system-wide generic setting
    return "default_setting"

# Call the function
setting = get_user_setting()
print(setting)  # Output will be the first non-None value found
