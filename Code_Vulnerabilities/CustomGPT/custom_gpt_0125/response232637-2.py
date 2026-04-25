
# MODULE1.py
colorLists = ['what is my color', 'color', 'red', 'pink', 'blue']

def check_color(name):
    return any(item in name for item in colorLists)

def get_color_response(name):
    name3 = input('What is your favorite color? ')
    if name3 == 'red':
        return 'You are hot!'
    elif name3 == 'pink':
        return 'You must be a lady'
    elif name3 == 'blue':
        return 'Boys love this'
    else:
        return 'Color not recognized.'
