
def run_module1(name):
    colorLists = ['what is my color', 'color']
    for item in name:
        if item in colorLists:
            print('You found the color here')
            name3 = input('What is your favorite color? ')
            if name3.lower() == 'red':
                print('You are hot!')
            elif name3.lower() == 'pink':
                print('You must be a lady')
            elif name3.lower() == 'blue':
                print('Boys love this')
            # Continue with more colors
