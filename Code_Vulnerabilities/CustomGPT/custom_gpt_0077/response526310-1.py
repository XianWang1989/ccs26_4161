
def get_screen_type():
    # Define functions to fetch settings
    def foo():
        # Retrieve user-specific setting
        pass

    def bar():
        # Retrieve account-wide setting
        pass

    def baz():
        # Retrieve system-wide setting
        pass

    # Create a generator of potential values
    settings = (foo(), bar(), baz())

    # Use next() to return the first truthy value, or a default if none
    return next((setting for setting in settings if setting), 'default_screen_type')
