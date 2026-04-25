
# MODULE1.py
def play_color_game():
    print("Welcome to the color game!")
    name = input('Please enter your question: ').lower()
    colorLists = ['red', 'pink', 'blue']

    for item in colorLists:
        if item in name:
            print(f'You found the color here: {item}')
            name3 = input('What is your favorite color? ').lower()
            if name3 == 'red':
                print('You are hot!')
            elif name3 == 'pink':
                print('You must be a lady.')
            elif name3 == 'blue':
                print('Boys love this!')
            return True  # Indicate that the game was played
    return False  # Indicate the game was not played
