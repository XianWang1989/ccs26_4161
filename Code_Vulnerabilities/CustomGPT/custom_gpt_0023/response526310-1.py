
def get_setting():
    functions = [foo, bar, baz]  # List of functions to check
    for func in functions:
        result = func()
        if result:
            return result
    return None  # or a default value if all checks fail
