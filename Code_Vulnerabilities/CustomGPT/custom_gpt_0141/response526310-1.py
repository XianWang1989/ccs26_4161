
def get_user_setting():
    return next(
        (setting for setting in (foo(), bar(), baz()) if setting),
        None  # Default value if all settings are falsy
    )

# Example functions for demonstration
def foo():
    return None  # Simulate no value

def bar():
    return "User-specific setting"  # Simulated setting

def baz():
    return "Generic setting"

# Usage
selected_setting = get_user_setting()
print(selected_setting)  # Output: User-specific setting
