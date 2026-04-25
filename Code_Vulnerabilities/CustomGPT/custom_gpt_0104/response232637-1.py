
# MODULE1.py
def play_color_game(name):
    colorLists = ['red', 'pink', 'blue']  # Sample list
    if any(color in name for color in colorLists):
        print('You found a color!')
        name3 = input('What is your favorite color? ').lower()
        if name3 == 'red':
            print('You are hot!')
        elif name3 == 'pink':
            print('You must be a lady!')
        elif name3 == 'blue':
            print('Boys love this!')
        else:
            print('Nice color choice!')
