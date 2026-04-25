
def play_color_game(user_input):
    colorLists = ['red', 'blue', 'pink']
    if any(color in user_input for color in colorLists):
        return "You found the color here!"
    return None
