
def foo():
    # Simulate retrieving a user-specific setting
    return None

def bar():
    # Simulate retrieving an account-wide setting
    return None

def baz():
    # Simulate retrieving a system-wide setting
    return "Default Screen Type"

# Define a list of functions to check in order of priority
settings_sources = [foo, bar, baz]

# Use a generator to get the first non-None result
result = next((setting() for setting in settings_sources if setting()), None)

# result will have the first valid setting or None if all fail
print(result)  # Output: "Default Screen Type"
