
# MODULE1.py
def handle_input(name):
    colorLists = ['what is my color', 'color', ...]
    if any(item in colorLists for item in name):
        print('You found the color here')
        name3 = input('What is your favorite color? ')
        if name3 == 'red':
            print('You are hot!')
        elif name3 == 'pink':
            print('You must be a lady')
        elif name3 == 'blue':
            print('Boys love this')
