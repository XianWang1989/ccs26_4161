
def get_setting():
    for func in [foo, bar, baz]:
        result = func()
        if result:
            return result
    return None  # Or a default value if all checks fail
