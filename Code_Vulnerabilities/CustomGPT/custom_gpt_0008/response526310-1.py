
def get_user_setting():
    # Define a list of functions to check in order
    check_functions = [foo, bar, baz]

    # Iterate through the functions and return the first truthy value
    for func in check_functions:
        result = func()
        if result:
            return result

    # Return a default value if none are found
    return None  # or any default value you want
