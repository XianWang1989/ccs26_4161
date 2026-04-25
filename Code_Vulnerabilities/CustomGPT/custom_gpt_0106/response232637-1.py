
def run_game(name):
    colorLists = ['red', 'pink', 'blue']  # Sample color list
    if name in colorLists:
        print(f'You found the color: {name}')
        name3 = input('What is your favorite color? ').strip()
        if name3 == 'red':
            print('You are hot!')
        elif name3 == 'pink':
            print('You must be a lady')
        elif name3 == 'blue':
            print('Boys love this')
