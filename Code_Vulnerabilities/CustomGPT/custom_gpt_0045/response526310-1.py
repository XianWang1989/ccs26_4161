
def get_screen_type():
    # Example functions simulating retrieval of settings
    def foo():
        return None  # Simulating a no-value case

    def bar():
        return "User-specific screen type"

    def baz():
        return "System-wide generic screen type"

    # List of functions to check in order of priority
    settings_checks = [foo, bar, baz]

    # Using next with a generator to return the first truthy result
    return next((setting() for setting in settings_checks if setting()), "Default screen type")

# Example of retrieving the screen type
screen_type = get_screen_type()
print(screen_type)  # Output: User-specific screen type
