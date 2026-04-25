
def foo():
    return None  # Assume this would return a specific user setting

def bar():
    return "Account-wide setting"  # Assume this is the account-wide screen type

def baz():
    return "System-wide generic setting"  # Generic fallback setting

result = get_setting()
print(result)  # Output will be "Account-wide setting"
