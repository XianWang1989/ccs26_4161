
def get_preferred_setting():
    # Define functions for retrieving the settings
    def foo():
        # Logic to get user-specific setting
        return None  # Example: No setting found

    def bar():
        # Logic to get account-wide setting
        return "Account-wide setting"  # Example: Found a setting

    def baz():
        # Logic to get system-wide generic setting
        return "System-wide default setting"  # Example: Default found

    # List of functions to check
    settings_checks = [foo, bar, baz]

    # Retrieve the first truthy result from the checks
    return next((setting() for setting in settings_checks if setting()), None)

# Usage
preferred_setting = get_preferred_setting()
print(preferred_setting)  # Output: "Account-wide setting"
