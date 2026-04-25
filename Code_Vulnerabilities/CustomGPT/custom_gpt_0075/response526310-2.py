
def get_setting():
    for func in (foo, bar, baz):
        var = func()
        if var:
            return var
    return None  # Fallback if all return None
