
def get_user_setting():
    # Define a list of functions to check
    funcs = [foo, bar, baz]

    # Use a generator expression and next to return the first value that is truthy
    return next((func() for func in funcs if func()), None)

# Example functions
def foo():
    return None  # Replace with actual logic

def bar():
    return None  # Replace with actual logic

def baz():
    return "default_setting"  # Replace with actual logic

# Usage
setting = get_user_setting()
print(setting)
