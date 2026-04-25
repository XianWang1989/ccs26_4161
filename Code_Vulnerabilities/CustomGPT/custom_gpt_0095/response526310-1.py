
def get_setting():
    # Simulated functions returning settings
    def foo(): return None  # User-specific setting
    def bar(): return "Account-wide setting"  # Account-wide setting
    def baz(): return "System-wide generic setting"  # Fallback setting

    # Priority list of functions to check
    settings_checks = [foo, bar, baz]

    # Use next() to find the first non-None result
    setting = next((func() for func in settings_checks if func() is not None), None)

    return setting

result = get_setting()
print(result)  # Output: "Account-wide setting"
