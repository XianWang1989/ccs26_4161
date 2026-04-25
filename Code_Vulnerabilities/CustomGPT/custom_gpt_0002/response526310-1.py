
def get_setting():
    for func in (foo, bar, baz):
        result = func()
        if result:
            return result
    return None  # Default return if no value is found
