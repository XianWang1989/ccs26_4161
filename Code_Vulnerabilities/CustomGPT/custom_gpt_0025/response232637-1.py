
def check_color(name):
    colorLists = ['what is my color', 'color']
    for item in colorLists:
        if item in name:
            return True, "You found the color here"
    return False, None
