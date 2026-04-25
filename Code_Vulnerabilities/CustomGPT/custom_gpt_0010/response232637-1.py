
# MODULE1.py
def run_module():
    question = input('What is your question? ').lower()
    colorLists = ['what is my color', 'color', 'red', 'pink', 'blue']
    for item in question.split():
        if item in colorLists:
            print('You found the color!')
            return True
    return False
