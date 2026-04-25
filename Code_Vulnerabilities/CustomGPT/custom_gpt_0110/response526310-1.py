
def get_screen_type():
    # Define the functions
    def foo():
        # Example implementation
        return None  # or a valid value

    def bar():
        # Example implementation
        return None  # or a valid value

    def baz():
        # Example implementation
        return "default_screen"  # or a valid value

    # List of functions to check
    functions = [foo, bar, baz]

    # Retrieve the first truthy value
    return next((func() for func in functions if func()), None)

# Usage
screen_type = get_screen_type()
print(screen_type)
