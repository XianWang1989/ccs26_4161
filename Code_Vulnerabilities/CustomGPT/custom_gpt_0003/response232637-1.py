
colorLists = ['what is my color', 'color', 'red', 'pink', 'blue']  # Sample list

def check_color(input_question):
    if any(color in input_question for color in colorLists):
        print("You found a color!")
        name3 = input("What is your favorite color?")
        if name3 == 'red':
            print('You are hot!')
        elif name3 == 'pink':
            print('You must be a lady')
        elif name3 == 'blue':
            print('Boys love this')
