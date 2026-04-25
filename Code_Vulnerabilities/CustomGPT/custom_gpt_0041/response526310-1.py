
def get_setting():
    return next((result for func in (foo, bar, baz) if (result := func())), None)
