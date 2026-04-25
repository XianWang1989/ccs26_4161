
def play():
    question = input('Please Enter your question: ').lower()
    colorLists = ['what is my color', 'color']
    if question in colorLists:
        print('You found the color here!')
