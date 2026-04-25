
def get_preferred_screen_type():
    screen_types = (foo, bar, baz)

    # Use next with a generator expression to find the first truthy value
    return next((var for func in screen_types if (var := func())) if var, None)

# Usage
preferred_screen_type = get_preferred_screen_type()
