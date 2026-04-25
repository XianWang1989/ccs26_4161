
def get_screen_type():
    def foo():
        # Logic to get user's specific screen type
        return None

    def bar():
        # Logic to get account-wide screen type
        return None

    def baz():
        # Logic to get system-wide generic screen type
        return "default_screen_type"

    # List of functions to check in order
    options = [foo, bar, baz]
    return next((func() for func in options if func()), None)

result = get_screen_type()
print(result)  # Output: "default_screen_type"
