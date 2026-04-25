
def get_preference():
    # Sample functions to retrieve settings
    def foo():
        return None  # User-specific setting

    def bar():
        return "account-wide setting"  # Account-wide setting

    def baz():
        return "generic setting"  # System-wide setting

    # List of functions to check in priority order
    preference_checkers = [foo, bar, baz]

    # Use next() to find the first non-None result
    return next((checker() for checker in preference_checkers if checker() is not None), None)

# Example usage
result = get_preference()
print(result)  # Outputs: account-wide setting
