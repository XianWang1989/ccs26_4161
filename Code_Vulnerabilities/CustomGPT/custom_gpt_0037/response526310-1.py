
def get_user_setting():
    # Define a list of functions to check
    check_functions = [foo, bar, baz]

    for func in check_functions:
        result = func()
        if result:
            return result

    return None  # Or a default value if needed
