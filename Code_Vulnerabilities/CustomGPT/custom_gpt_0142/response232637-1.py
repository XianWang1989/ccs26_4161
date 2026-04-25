
# MODULE1.py

def check_color_response(name):
    colorLists = ['what is my color', 'color', 'red', 'pink', 'blue']
    if name in colorLists:
        print('You found the color here')
        name3 = input('What is your favorite color? ')
        if name3.lower() == 'red':
            print('You are hot!')
        elif name3.lower() == 'pink':
            print('You must be a lady')
        elif name3.lower() == 'blue':
            print('Boys love this')
