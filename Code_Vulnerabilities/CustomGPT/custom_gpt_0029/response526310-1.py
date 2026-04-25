
def get_setting():
    # Example functions simulating user setting retrieval
    def foo():
        return None  # Replace with actual logic

    def bar():
        return "User Specific Setting"

    def baz():
        return "Account-Wide Setting"

    # List of functions to check
    settings_checks = [foo, bar, baz]

    # Use next to return the first truthy value
    return next((setting() for setting in settings_checks if setting()), None)

# Usage
final_setting = get_setting()
print(final_setting)  # Outputs: "User Specific Setting"
