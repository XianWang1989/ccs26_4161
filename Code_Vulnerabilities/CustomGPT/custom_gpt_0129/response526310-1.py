
def get_setting():
    for func in (foo, bar, baz):
        var = func()
        if var:
            return var
    return None # Or some default value if none of the functions return a truthy value

# Example mock functions for demonstration
def foo():
    return None  # Represents no setting for user

def bar():
    return None  # Represents no account-wide setting

def baz():
    return "generic_setting"  # Represents the system-wide generic setting

# Usage
result = get_setting()
print(result)  # Output: 'generic_setting'
