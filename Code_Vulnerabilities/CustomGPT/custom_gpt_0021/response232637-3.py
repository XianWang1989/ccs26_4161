
# MODULE1.py
def run_module(name):
    colorLists = ['what is my color', 'color']
    if name in colorLists:
        name3 = input('What is your favorite color? ')
        if name3.lower() == 'red':
            print('You are hot!')
        elif name3.lower() == 'pink':
            print('You must be a lady')
        elif name3.lower() == 'blue':
            print('Boys love this!')
