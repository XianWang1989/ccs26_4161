
def get_user_setting():
    # Define the ordered list of functions to check
    check_functions = [foo, bar, baz]  # Add more functions as needed

    # Iterate through each function and return the first truthy value
    for func in check_functions:
        result = func()
        if result:
            return result

    return None  # Or some default value if all checks return None or falsy

# Example function definitions (to illustrate)
def foo():
    return None  # Placeholder for actual logic

def bar():
    return None  # Placeholder for actual logic

def baz():
    return 'default_screen_type'  # Return a valid value

# Usage
setting = get_user_setting()
print(setting)  # Output: 'default_screen_type' (or the output of the first truthy function)
