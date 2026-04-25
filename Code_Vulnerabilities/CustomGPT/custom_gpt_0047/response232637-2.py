
# MODULE1.py
colorLists = ['what is my color', 'color', 'red', 'blue', 'pink']

def process_question(question):
    if any(item in question for item in colorLists):
        name3 = input('What is your favorite color? ')
        if name3 == 'red':
            print('You are hot!')
        elif name3 == 'pink':
            print('You must be a lady!')
        elif name3 == 'blue':
            print('Boys love this!')
        else:
            print('That\'s an interesting choice!')
        return True  # Indicates this module handled the question
    return False  # Indicates this module did not handle it
