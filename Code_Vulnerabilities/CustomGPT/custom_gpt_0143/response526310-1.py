
def get_setting():
    for func in (foo, bar, baz):
        var = func()
        if var:
            return var
    return None  # Or a default value if needed
