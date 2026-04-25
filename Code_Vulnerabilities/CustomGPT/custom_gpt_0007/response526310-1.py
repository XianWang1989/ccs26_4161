
def get_user_setting():
    return next((
        value for func in (foo, bar, baz) 
        for value in (func(),) if value
    ), None)
