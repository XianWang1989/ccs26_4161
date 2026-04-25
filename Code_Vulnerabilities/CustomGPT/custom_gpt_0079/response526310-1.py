
def get_user_setting():
    # Define your functions to retrieve settings
    def foo():
        # Retrieve user-specific screen type
        return None  # Replace with actual logic

    def bar():
        # Retrieve account-wide screen type
        return None  # Replace with actual logic

    def baz():
        # Retrieve system-wide generic screen type
        return "default_screen"  # Replace with actual logic

    # Create a generator of the functions
    settings = (foo(), bar(), baz())

    # Use next() with a default value if all return None
    return next((setting for setting in settings if setting is not None), "default_screen")

# Example usage
screen_type = get_user_setting()
