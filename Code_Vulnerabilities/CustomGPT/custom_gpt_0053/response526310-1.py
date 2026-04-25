
def get_setting():
    settings_check = (func() for func in (foo, bar, baz))
    return next((result for result in settings_check if result), None)

var = get_setting()
