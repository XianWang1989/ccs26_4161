
def get_setting():
    checks = [foo, bar, baz]

    for check in checks:
        var = check()
        if var:
            return var

    return None  # or a default value if needed

# Usage
setting = get_setting()
