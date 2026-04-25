
def get_preferred_setting():
    for func in (foo, bar, baz):
        value = func()
        if value:
            return value
    return None  # Return None if all functions return falsy values
