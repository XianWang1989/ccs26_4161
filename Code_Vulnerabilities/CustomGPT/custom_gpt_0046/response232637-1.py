
# MODULE1.py
def run(question):
    colorLists = ['red', 'blue', 'pink']
    if any(color in question for color in colorLists):
        print('You found a color!')
        # Additional color logic here
        return True
    return False
