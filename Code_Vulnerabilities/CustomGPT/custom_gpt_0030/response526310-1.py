
def get_user_setting():
    return next((func() for func in (foo, bar, baz) if func()), None)

# Example functions
def foo():
    # Retrieve user-specific setting
    return None  # No value found

def bar():
    # Retrieve account-wide setting
    return "account-wide setting"

def baz():
    # Retrieve system-wide setting
    return "system-wide setting"

# Usage
setting = get_user_setting()
print(setting)  # Outputs: "account-wide setting"
