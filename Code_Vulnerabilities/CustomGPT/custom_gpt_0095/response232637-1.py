
# MODULE1.py
def play_game():
    name = input('Please Enter your question: ').lower()
    colorList = ['red', 'blue', 'pink']
    if name in colorList:
        name3 = input('What is your favorite color? ')
        if name3 == 'red':
            print('You are hot!')
        elif name3 == 'pink':
            print('You must be a lady!')
        elif name3 == 'blue':
            print('Boys love this!')
