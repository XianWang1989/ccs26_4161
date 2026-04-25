
colorLists = ['red', 'pink', 'blue', 'green']  # Example of the question-list

def check_answer(question):
    return any(color in question for color in colorLists)

def respond():
    name3 = input('What is your favorite color? ')
    if name3 == 'red':
        print('You are hot!')
    elif name3 == 'pink':
        print('You must be a lady')
    elif name3 == 'blue':
        print('Boys love this')
    else:
        print("I don't know that color.")
