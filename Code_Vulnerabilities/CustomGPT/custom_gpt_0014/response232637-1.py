
def handle_question(question):
    color_list = ['what is my color', 'color']
    if question in color_list:
        color = input('What is your favorite color? ')
        if color == 'red':
            print('You are hot!')
        elif color == 'pink':
            print('You must be a lady!')
        elif color == 'blue':
            print('Boys love this!')
