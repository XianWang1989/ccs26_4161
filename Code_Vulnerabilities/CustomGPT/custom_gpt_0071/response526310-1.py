
def get_setting():
    for func in (foo, bar, baz):
        result = func()
        if result:
            return result
    return None  # In case all checks fail

# Usage example
setting = get_setting()
