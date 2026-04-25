
def play_color_game(user_input):
    color_lists = ['what is my color', 'color']
    if user_input in color_lists:
        name3 = input('What is your favorite color? ')
        if name3 == 'red':
            print('You are hot!')
        elif name3 == 'pink':
            print('You must be a lady!')
        elif name3 == 'blue':
            print('Boys love this!')
