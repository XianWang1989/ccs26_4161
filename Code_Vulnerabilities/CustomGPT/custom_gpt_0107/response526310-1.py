
def get_user_setting():
    # Attempt to retrieve the user-specific setting
    return foo() or bar() or baz() or default_setting()

def default_setting():
    # Return the system-wide generic setting
    return "generic_screen_type"

# Usage
screen_type = get_user_setting()
