
def foo():
    return None  # User-specific setting

def bar():
    return "account-wide setting"  # Account-wide setting

def baz():
    return "system-wide generic setting"  # Generic setting

setting = next((value for func in (foo, bar, baz) if (value := func())), None)
print(setting)  # Outputs: "account-wide setting"
