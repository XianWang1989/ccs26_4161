
def play_game(name):
    colorLists = ['red', 'green', 'blue']  # Example color list
    if any(color in name for color in colorLists):
        name3 = input('What is your favorite color? ')
        if name3 == 'red':
            print('You are hot!')
        elif name3 == 'green':
            print('You are calm!')
        elif name3 == 'blue':
            print('Boys love this!')
