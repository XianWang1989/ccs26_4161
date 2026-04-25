
def get_screen_type():
    # Define your functions to retrieve settings
    def foo():
        # Retrieve user-specific setting
        return None  # Placeholder for an actual value or None if not set

    def bar():
        # Retrieve account-wide setting
        return None  # Placeholder for the actual value

    def baz():
        # Retrieve system-wide generic setting
        return "generic_screen"  # Example return value

    # Use a generator to find the first valid setting
    return next((setting for setting in (foo(), bar(), baz()) if setting is not None), None)

# Example usage
screen_type = get_screen_type()
print(screen_type)  # Outputs the first non-None value
