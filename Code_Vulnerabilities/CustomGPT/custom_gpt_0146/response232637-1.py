
def run_game():
    print("You are in MODULE1: Color Game")
    name = input('Please enter your question: ').lower()
    colorLists = ['red', 'pink', 'blue']  # Example color list

    if any(color in name for color in colorLists):
        name3 = input('What is your favorite color? ')
        if name3 == 'red':
            print('You are hot!')
        elif name3 == 'pink':
            print('You must be a lady!')
        elif name3 == 'blue':
            print('Boys love this!')
