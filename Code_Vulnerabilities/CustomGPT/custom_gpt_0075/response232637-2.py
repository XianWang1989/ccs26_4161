
# MODULE1.py
def handle_question(question):
    colorLists = ['what is my color', 'color']
    if question in colorLists:
        print('You found the color here!')
        name3 = input('What is your favorite color? ')
        if name3 == 'red':
            print('You are hot!')
        elif name3 == 'pink':
            print('You must be a lady!')
        elif name3 == 'blue':
            print('Boys love this!')
