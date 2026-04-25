
colorLists = ['red', 'blue', 'pink', 'yellow']  # Sample color list

def process(name2):
    for item in name2:
        if item in colorLists:
            print('You found the color here')
            name3 = input('What is your favorite color? ')
            respond_to_color(name3)

def respond_to_color(color):
    if color == 'red':
        print('You are hot!')
    elif color == 'pink':
        print('You must be a lady')
    elif color == 'blue':
        print('Boys love this')
    # Add more responses as needed
