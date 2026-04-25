
def get_setting():
    return next(
        (setting for func in (foo, bar, baz) if (setting := func())),
        None  # Default value if all return None
    )
