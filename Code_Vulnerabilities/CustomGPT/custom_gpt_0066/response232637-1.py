
def process_input(user_input):
    colorLists = ['what is my color', 'color', 'red', 'blue', 'pink']
    if user_input in colorLists:
        print('You found the color here!')
        name3 = input('What is your favorite color? ').lower()
        if name3 == 'red':
            print('You are hot!')
        elif name3 == 'pink':
            print('You must be a lady')
        elif name3 == 'blue':
            print('Boys love this')
