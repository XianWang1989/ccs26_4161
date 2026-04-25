
def process_input(user_input):
    carLists = ['what is my car', 'car', 'toyota', 'ford']
    if user_input in carLists:
        print('You found a car!')
        name3 = input('What is your favorite car? ').lower()
        print(f'You love {name3}!')
