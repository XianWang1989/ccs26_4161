
# MODULE1.py
def game_logic(name):
    color_list = ['red', 'pink', 'blue']
    for item in color_list:
        if item in name:
            print(f'You found the color: {item}')
            return True
    return False
