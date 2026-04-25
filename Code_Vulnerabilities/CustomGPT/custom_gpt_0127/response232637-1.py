
def run():
    name = input('Please enter your question: ').lower()
    colorLists = ['red', 'blue', 'pink']
    if any(color in name for color in colorLists):
        print('You found a color here!')
