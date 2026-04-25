
def get_preferred_setting():
    functions = [foo, bar, baz]  # List of functions to check
    for func in functions:
        result = func()
        if result:
            return result
    return None  # Default if none return a truthy value

# Usage
preferred_setting = get_preferred_setting()
