
def get_user_setting():
    settings_checks = [foo, bar, baz]

    for check in settings_checks:
        result = check()
        if result:
            return result

    return None  # or a default value if all checks fail
