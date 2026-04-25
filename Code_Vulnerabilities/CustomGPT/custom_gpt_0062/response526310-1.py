
def get_setting():
    return next((func() for func in (foo, bar, baz) if func()), None)
