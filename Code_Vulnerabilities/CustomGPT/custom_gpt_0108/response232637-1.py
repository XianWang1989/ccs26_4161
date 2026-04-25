
# MODULE1.py
def play_game(name):
    color_lists = ['what is my color', 'color']
    if name in color_lists:
        print('You found the color game!')
        name3 = input('What is your favorite color? ').lower()
        if name3 == 'red':
            print('You are hot!')
        elif name3 == 'pink':
            print('You must be a lady!')
        # Add more colors as needed
