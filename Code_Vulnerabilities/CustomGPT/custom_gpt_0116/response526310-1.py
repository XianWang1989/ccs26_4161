
def foo():
    # logic for foo
    return None

def bar():
    # logic for bar
    return None

def baz():
    # logic for baz
    return None

def get_setting():
    for func in [foo, bar, baz]:
        result = func()
        if result:
            return result
    return None  # Default case if all checks fail

# Example usage
setting = get_setting()
print(setting)
