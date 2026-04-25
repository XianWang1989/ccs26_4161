
def check_color(name2):
    colorLists = ['what is my color', 'color']
    for item in name2:
        if item in colorLists:
            return True, 'color'
    return False, None
