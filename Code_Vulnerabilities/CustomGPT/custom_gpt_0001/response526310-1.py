
def get_screen_type():
    # Simulate the setting retrieval functions
    def foo():
        # Example: returns None (no user-specific setting)
        return None

    def bar():
        # Example: returns None (no account-wide setting)
        return None

    def baz():
        # Example: returns 'generic' (system-wide setting)
        return 'generic'

    # Create a list of functions to check
    funcs = [foo, bar, baz]

    # Use a generator expression to get the first truthy value from the functions
    return next((func() for func in funcs if func()), None)

# Example usage
screen_type = get_screen_type()
print(screen_type)  # Output: 'generic'
