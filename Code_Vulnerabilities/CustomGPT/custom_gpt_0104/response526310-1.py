
def get_screen_type():
    return next((result for result in (foo(), bar(), baz()) if result), None)

screen_type = get_screen_type()
