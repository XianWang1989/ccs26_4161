
# MODULE1.py
def play_game(name):
    colorLists = ['what is my color', 'color', 'red', 'blue', 'pink']
    if any(item in colorLists for item in name.split()):
        print('You found the color here!')
        name3 = input('What is your favorite color? ').strip().lower()
        if name3 == 'red':
            print('You are hot!')
        elif name3 == 'pink':
            print('You must be a lady!')
        elif name3 == 'blue':
            print('Boys love this!')
