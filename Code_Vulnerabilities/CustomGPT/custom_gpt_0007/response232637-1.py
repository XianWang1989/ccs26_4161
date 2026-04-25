
def run_module1():
    import re
    name = input('Please Enter your question: ').lower()
    colorLists = ['what is my color', 'color']
    if any(item in name for item in colorLists):
        print('You found the color here')
        name3 = input('What is your favorite color? ')
        # Further logic can follow...
