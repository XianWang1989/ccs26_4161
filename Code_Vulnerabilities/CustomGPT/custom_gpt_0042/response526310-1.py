
def get_screen_type():
    # Define your functions that retrieve settings
    def foo():
        return None  # Replace with actual logic

    def bar():
        return None  # Replace with actual logic

    def baz():
        return "generic_setting"  # Replace with actual logic

    # Create a generator for the functions
    settings = (foo(), bar(), baz())

    # Return the first truthy value or a default if none found
    return next((setting for setting in settings if setting), "default_setting")

# Example usage
screen_type = get_screen_type()
print(screen_type)
