
def handle_question(question):
    color_lists = ['what is my color', 'color']
    if question in color_lists:
        print('You found the color here')
        name3 = input('What is your favorite color? ')
        if name3.lower() == 'red':
            print('You are hot!')
        elif name3.lower() == 'pink':
            print('You must be a lady')
        elif name3.lower() == 'blue':
            print('Boys love this')
