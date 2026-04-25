
def get_setting():
    # Define a list of functions to check
    checks = [foo, bar, baz]

    # Use next() to return the first truthy result
    return next((check() for check in checks if check()), None)

# Example functions for demonstration
def foo():
    return None  # Simulating no user setting

def bar():
    return "account-wide setting"  # Simulating account-wide setting

def baz():
    return "generic setting"  # Simulating generic setting

# Call the function
result = get_setting()
print(result)  # Output will be "account-wide setting"
