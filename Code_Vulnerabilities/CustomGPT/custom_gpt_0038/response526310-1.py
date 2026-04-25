
def get_user_setting():
    return (val for func in (foo, bar, baz) if (val := func()) is not None)

# Get the first non-None value from the checks
selected_setting = next(get_user_setting(), default_value)

return selected_setting
