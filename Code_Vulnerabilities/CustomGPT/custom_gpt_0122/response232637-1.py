
# MODULE1.py
def handle_input(user_input):
    colorLists = ['what is my color', 'color']
    if user_input in colorLists:
        print('You found the color here!')
        favorite_color = input('What is your favorite color? ')
        respond_to_color(favorite_color)

def respond_to_color(color):
    if color == 'red':
        print('You are hot!')
    elif color == 'pink':
        print('You must be a lady.')
    elif color == 'blue':
        print('Boys love this.')
