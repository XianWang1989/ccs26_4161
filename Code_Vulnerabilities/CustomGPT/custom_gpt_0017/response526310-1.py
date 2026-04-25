
def get_setting():
    def foo():
        # Retrieve user-specific screen type
        pass

    def bar():
        # Retrieve account-wide screen type
        pass

    def baz():
        # Retrieve system-wide generic screen type
        pass

    for func in [foo, bar, baz]:
        result = func()
        if result:
            return result

    return None  # Default case if all checks fail
