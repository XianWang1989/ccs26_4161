
def play_game():
    color_lists = ['what is my color', 'color']
    name = input('Please Enter your question: ').lower()
    if any(item in name for item in color_lists):
        print('You found the color here')
        name3 = input('What is your favorite color? ')
        if name3 == 'red':
            print('You are hot!')
        elif name3 == 'pink':
            print('You must be a lady!')
        # Add more conditions as needed
