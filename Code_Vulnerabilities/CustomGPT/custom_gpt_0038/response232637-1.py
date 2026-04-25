
def handle_color_question(name):
    color_lists = ['what is my color', 'color', 'red', 'pink', 'blue']
    for item in color_lists:
        if item in name:
            print('You found the color here')
            name3 = input('What is your favorite color? ').lower()
            # Additional responses based on user input
            if name3 == 'red':
                print('You are hot!')
            elif name3 == 'pink':
                print('You must be a lady')
            elif name3 == 'blue':
                print('Boys love this')
