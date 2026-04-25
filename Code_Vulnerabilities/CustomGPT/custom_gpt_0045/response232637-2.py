
def run_module(name):
    foodLists = ['what is your favorite food', 'food', 'pizza']
    if name in foodLists:
        print('You like food!')
        name3 = input('What is your favorite food? ')
        print(f'I also like {name3}!')
