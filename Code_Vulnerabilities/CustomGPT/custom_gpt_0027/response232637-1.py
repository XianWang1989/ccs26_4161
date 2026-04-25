
def run_game(user_input):
    colorLists = ['red', 'blue', 'pink']  # Sample colors
    for item in user_input:
        if item in colorLists:
            print(f'You found the color: {item}')
