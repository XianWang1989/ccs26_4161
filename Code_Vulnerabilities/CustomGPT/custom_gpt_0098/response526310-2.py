
def get_user_setting():
    return next((result for func in (foo, bar, baz, ..., func100) if (result := func())), None)
