
def foo():
    # Simulate retrieving a user-specific setting
    return None  # Assume the user-specific setting is not set

def bar():
    # Simulate retrieving an account-wide setting
    return None  # Assume the account-wide setting is not set

def baz():
    # Simulate retrieving a system-wide setting
    return "Generic Screen Type"  # This is the default/fallback setting

# List of functions to check in order of priority
functions_to_check = [foo, bar, baz]

# Retrieve the first non-None value from the functions
result = next((func() for func in functions_to_check if func() is not None), None)

print(result)  # Output will be "Generic Screen Type" in this case
