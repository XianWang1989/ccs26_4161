
def run():
    name = input('Please Enter your question: ').lower()
    carLists = ['what is my favorite car', 'car']

    if any(item in carLists for item in name.split()):
        print('You found the car here!')
        name3 = input('What is your favorite car? ')
        print(f'You chose: {name3}')
