
def get_screen_type():
    # Define a list of functions to check
    funcs = [foo, bar, baz]

    # Use next with a generator to fetch the first truthy value
    return next((result for func in funcs if (result := func())), None)
