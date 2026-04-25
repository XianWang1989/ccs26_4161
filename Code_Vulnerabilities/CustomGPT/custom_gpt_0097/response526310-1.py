
def get_setting():
    for func in (foo, bar, baz):
        var = func()
        if var:
            return var
    return None  # Default case if all checks fail
