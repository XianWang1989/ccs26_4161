
def check_color_question(name):
    colorLists = ['what is my color', 'color', 'red', 'blue', 'pink']
    if any(item in name for item in colorLists):
        return "You found the color here"
    return None
