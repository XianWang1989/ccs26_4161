
def run():
    name = input('Please Enter your question: ').lower()
    colorLists = ['red', 'blue', 'pink']  # Sample color list
    if any(color in name for color in colorLists):
        print('You found the color here!')
