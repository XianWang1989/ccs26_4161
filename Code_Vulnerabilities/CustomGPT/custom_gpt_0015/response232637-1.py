
# MODULE1.py
def handle_color(name):
    colorLists = ['what is my color', 'color']  # Add more colors
    if name in colorLists:
        print('You found the color here')
        name3 = input('What is your favorite color? ')
        if name3.lower() == 'red':
            print('You are hot!')
        # Add more conditions for other colors
