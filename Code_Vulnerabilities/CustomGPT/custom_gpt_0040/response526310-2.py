
def foo():
    # User-specific setting
    return None  # Simulating no value found

def bar():
    # Account-wide setting
    return 'account-wide setting'

def baz():
    # System-wide generic setting
    return 'generic setting'

preferred_setting = get_preferred_setting()
print(preferred_setting)  # Output: 'account-wide setting'
