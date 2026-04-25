
def play_color_game(name):
    colorLists = ['red', 'pink', 'blue']
    for item in colorLists:
        if item in name:
            print(f'You found the color: {item}')
            name3 = input('What is your favorite color? ').lower()
            if name3 == 'red':
                print('You are hot!')
            elif name3 == 'pink':
                print('You must be a lady.')
            elif name3 == 'blue':
                print('Boys love this!')
