
def check_color(name):
    color_lists = ['what is my color', 'color']
    if any(item in color_lists for item in name):
        print('You found the color here')
        # Additional logic for colors...
