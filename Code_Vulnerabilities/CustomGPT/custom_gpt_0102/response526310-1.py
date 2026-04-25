
def get_setting():
    def foo():
        # Logic for foo
        return None

    def bar():
        # Logic for bar
        return None

    def baz():
        # Logic for baz
        return "user_specific_setting"

    # List of functions to check in order of priority
    settings_checks = [foo, bar, baz]

    # Return the first truthy result from the settings checks
    return next((setting() for setting in settings_checks if setting()), "default_setting")

# Usage
result = get_setting()
print(result)  # Output: "user_specific_setting" or "default_setting"
