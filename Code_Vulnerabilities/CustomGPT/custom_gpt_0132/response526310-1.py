
def get_setting():
    settings_checks = [foo, bar, baz]

    return next((func() for func in settings_checks if func()), None)

result = get_setting()
