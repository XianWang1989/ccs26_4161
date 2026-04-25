
def get_setting():
    for func in (foo, bar, baz):
        var = func()
        if var:
            return var
    return None  # Optional: to indicate no valid setting was found
