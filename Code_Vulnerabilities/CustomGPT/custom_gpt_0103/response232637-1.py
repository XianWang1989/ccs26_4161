
def play_color_game():
    name = input('Please Enter your question: ').lower()
    color_list = ['red', 'pink', 'blue']

    if any(color in name for color in color_list):
        print('You found the color here!')
        name3 = input('What is your favorite color? ').lower()
        responses = {
            'red': 'You are hot!',
            'pink': 'You must be a lady!',
            'blue': 'Boys love this!'
        }
        print(responses.get(name3, 'I do not know that color!'))

