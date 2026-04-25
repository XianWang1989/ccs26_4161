
def play_game(input_string):
    colorLists = ['red', 'blue', 'pink']
    if any(color in input_string for color in colorLists):
        print('You found a color! What is your favorite color?')

        name3 = input('Please enter your favorite color: ')
        if name3 == 'red':
            print('You are hot!')
        elif name3 == 'pink':
            print('You must be a lady')
        elif name3 == 'blue':
            print('Boys love this')
        else:
            print('Color not recognized.')
