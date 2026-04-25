
def run():
    colorLists = ['what is my color', 'color']  # Add more sample lists
    name = input('Please enter your question: ').lower()

    if name in colorLists:
        print('You found the color here')
        name3 = input('What is your favorite color?')
        if name3 == 'red':
            print('You are hot!')
        elif name3 == 'pink':
            print('You must be a lady')
        elif name3 == 'blue':
            print('Boys love this')
        # Add more colors as needed
