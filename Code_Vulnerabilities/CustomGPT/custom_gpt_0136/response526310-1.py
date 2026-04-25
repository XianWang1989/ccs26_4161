
def get_screen_type():
    def foo():
        # Example implementation
        return None  # User-specific setting

    def bar():
        # Example implementation
        return None  # Account-wide setting

    def baz():
        # Example implementation
        return 'generic'  # System-wide setting

    # Uses a generator expression to find the first truthy value
    return next((var for var in (foo(), bar(), baz()) if var), None)

screen_type = get_screen_type()
print(screen_type)  # Output will be 'generic' in this case
