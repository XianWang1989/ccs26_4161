
colorLists = ['red', 'pink', 'blue']

def run_game():
    name = input('Please Enter your question: ').lower()
    for item in name.split():
        if item in colorLists:
            name3 = input('What is your favorite color? ')
            if name3 == 'red':
                print('You are hot!')
            elif name3 == 'pink':
                print('You must be a lady')
            elif name3 == 'blue':
                print('Boys love this')
            # Continue with more colors
            return True  # Indicate that the game found a match
    return False  # No match found
