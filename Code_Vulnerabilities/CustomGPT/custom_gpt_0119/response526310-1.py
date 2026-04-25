
def get_user_setting():
    return (value for func in (foo, bar, baz) if (value := func()) is not None)

# Retrieve the first non-None value from the functions
result = next(get_user_setting(), default_value)

# Use the result
return result
