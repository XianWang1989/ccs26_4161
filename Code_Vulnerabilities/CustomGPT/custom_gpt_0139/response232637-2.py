
def run_module(name):
    carLists = ['what is your favorite car', 'car', 'toyota', 'ford']

    if name in carLists:
        print('You found a car!')
        name3 = input('What is your favorite car? ').lower()
        print(f'You chose {name3}!')
        # Add more responses as needed
