
def get_user_setting():
    # Define your functions
    def foo():
        # Logic for foo
        return None  # Example return value

    def bar():
        # Logic for bar
        return None  # Example return value

    def baz():
        # Logic for baz
        return "Preferred setting"  # Example return value

    # List of functions to check
    checks = [foo, bar, baz]

    # Use next with a generator expression
    return next((func() for func in checks if func()), None)

# Example usage
result = get_user_setting()
print(result)  # Outputs: "Preferred setting"
