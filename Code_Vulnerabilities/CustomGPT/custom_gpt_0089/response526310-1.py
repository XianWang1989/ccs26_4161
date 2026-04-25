
def get_setting():
    settings_sources = [foo, bar, baz]

    # Use next to yield the first truthy result or None if all are falsy
    return next((source() for source in settings_sources if source()), None)

# Example functions (foo, bar, baz) for illustration
def foo():
    return None

def bar():
    return "User-specific setting"

def baz():
    return "System-wide setting"

# Get the setting
result = get_setting()
print(result)  # Output: "User-specific setting"
