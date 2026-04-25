
def game(color_input):
    colorLists = ['what is my color', 'color', ...]  # Add your color phrases here
    if color_input in colorLists:
        response = input('What is your favorite color? ').lower()
        if response == 'red':
            print('You are hot!')
        elif response == 'pink':
            print('You must be a lady')
        elif response == 'blue':
            print('Boys love this')
