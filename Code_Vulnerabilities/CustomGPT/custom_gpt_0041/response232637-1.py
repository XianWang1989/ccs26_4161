
def check_color(name):
    color_lists = ['what is my color', 'color', 'red', 'pink', 'blue']
    if any(item in color_lists for item in name):
        return True
    return False
