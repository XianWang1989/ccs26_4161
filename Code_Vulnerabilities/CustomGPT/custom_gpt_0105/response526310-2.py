
def get_setting():
    return next(
        (result for func in (foo, bar, baz, func4, func5, ...) if (result := func())),
        None
    )
