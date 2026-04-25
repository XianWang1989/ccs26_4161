
def get_user_setting():
    check_functions = [foo, bar, baz]
    for func in check_functions:
        setting = func()
        if setting:
            return setting
    return None  # Default if all checks fail
