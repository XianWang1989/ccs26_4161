
def play_color_game(name):
    colorLists = ['what is my color', 'color', ...] # your 5mb list
    if any(item in name for item in colorLists):
        print('You found the color here')
        name3 = input('What is your favorite color? ')
        # More color checks...
