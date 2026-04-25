
def get_user_setting():
    # Placeholder implementations for the functions
    return None  # User-specific setting

def get_account_setting():
    return None  # Account-wide setting

def get_system_setting():
    return "default_screen_type"  # System-wide generic setting

def retrieve_setting():
    # List of functions to check in order of priority
    settings_check = [get_user_setting, get_account_setting, get_system_setting]

    # Use next() to return the first truthy value or a default if none found
    return next((setting() for setting in settings_check if setting()), "default_screen_type")

# Example usage
screen_type = retrieve_setting()
print(screen_type)
