
def run():
    name = input('Please Enter your question: ').lower()
    colorLists = ['what is my color', 'color']

    if any(item in colorLists for item in name.split()):
        print('You found the color here!')
        name3 = input('What is your favorite color? ')
        print(f'You chose: {name3}')
