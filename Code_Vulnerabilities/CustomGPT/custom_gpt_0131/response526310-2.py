
def get_user_setting():
    funcs = [foo, bar, baz]  # Add more functions as needed
    return next((func() for func in funcs if func()), None)

# Usage
result = get_user_setting()
if result:
    return result
