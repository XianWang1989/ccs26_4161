
def foo():
    return None

def bar():
    return "User-specific setting"

def baz():
    return "Generic setting"

setting = get_setting()
print(setting)  # Output will be "User-specific setting"
