
# MODULE1.py
def play_color_game():
    name = input('Please enter your question: ').lower()
    color_lists = ['what is my color', 'color', ...]  # Add your color questions here
    if any(item in name for item in color_lists):
        name3 = input('What is your favorite color? ')
        if name3 == 'red':
            print('You are hot!')
        elif name3 == 'pink':
            print('You must be a lady')
        elif name3 == 'blue':
            print('Boys love this')
