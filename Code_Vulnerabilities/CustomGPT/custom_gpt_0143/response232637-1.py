
def play_game(name):
    color_lists = ['what is my color', 'color']
    if name in color_lists:
        response = input('What is your favorite color? ')
        if response == 'red':
            print('You are hot!')
        elif response == 'pink':
            print('You must be a lady.')
        elif response == 'blue':
            print('Boys love this.')
        else:
            print('Color not recognized.')
