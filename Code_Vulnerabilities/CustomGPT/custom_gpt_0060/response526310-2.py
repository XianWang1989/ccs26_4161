
def get_user_setting():
    settings_sources = [foo, bar, baz]  # List of functions to check
    return next(
        (func() for func in settings_sources if func()),
        None
    )

result = get_user_setting()
if result is not None:
    return result
