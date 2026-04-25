
def check_color(name2):
    colorLists = ['red', 'pink', 'blue']
    for item in name2:
        if item in colorLists:
            print('You found the color here')
            return True
    return False
