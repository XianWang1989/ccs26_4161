
def check_color(name):
    colorLists = ['what is my color', 'color']
    if any(item in name for item in colorLists):
        return 'color'
    return None
