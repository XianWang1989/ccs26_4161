
def check_colors(name):
    color_lists = ['red', 'pink', 'blue']
    for item in name:
        if item in color_lists:
            print(f'Found a color: {item}')
            return True
    return False
