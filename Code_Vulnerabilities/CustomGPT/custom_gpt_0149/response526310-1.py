
def get_setting():
    for func in (foo, bar, baz):
        var = func()
        if var:
            return var
    return None  # or a default value if all checks fail

# Usage
setting = get_setting()
