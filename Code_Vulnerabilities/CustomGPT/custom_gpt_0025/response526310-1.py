
def get_screen_type():
    return next(
        (result for func in (foo, bar, baz) if (result := func())),
        None  # Default value if all are falsy
    )
