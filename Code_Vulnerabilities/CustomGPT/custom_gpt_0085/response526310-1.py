
def get_setting():
    # Define your functions that return values
    def foo():
        # User-specific setting
        return None  # Replace with actual logic

    def bar():
        # Account-wide setting
        return None  # Replace with actual logic

    def baz():
        # System-wide generic setting
        return "default_setting"  # Replace with actual logic

    # List of functions to check in order of priority
    funcs = [foo, bar, baz]

    # Use next to find the first non-falsy return value
    return next((func() for func in funcs if func()), None)

# Example usage
result = get_setting()
print(result)  # Output will be the first non-falsy setting or None
