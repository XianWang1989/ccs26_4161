
def process_question(question):
    color_list = ['red', 'pink', 'blue']  # Example list
    if any(color in question for color in color_list):
        print('You found a color!')
        name3 = input('What is your favorite color? ').lower()
        if name3 == 'red':
            print('You are hot!')
        elif name3 == 'pink':
            print('You must be a lady')
        elif name3 == 'blue':
            print('Boys love this')
        return True
    return False
