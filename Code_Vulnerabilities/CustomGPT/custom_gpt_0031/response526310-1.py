
def get_screen_type():
    return next((func() for func in (foo, bar, baz) if func()), None)

# Example functions
def foo():
    # Example user-specific setting
    return None  # Simulate that this setting is not set

def bar():
    # Example account-wide setting
    return "Account-wide setting"

def baz():
    # Example system-wide setting
    return "System-wide generic setting"

# Usage
screen_type = get_screen_type()
print(screen_type)  # Output: "Account-wide setting"
