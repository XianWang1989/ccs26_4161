
def handle_input(name):
    colorLists = ['red', 'pink', 'blue', 'yellow', 'green']
    if any(item in colorLists for item in name):
        print('You found a color here!')
        name3 = input('What is your favorite color? ')
        if name3 == 'red':
            print('You are hot!')
        elif name3 == 'pink':
            print('You must be a lady!')
        elif name3 == 'blue':
            print('Boys love this!')
