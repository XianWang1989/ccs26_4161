
def get_user_preference():
    preference_checkers = [foo, bar, baz]
    for check in preference_checkers:
        var = check()
        if var:
            return var
    return None  # Default return if no preference is found
