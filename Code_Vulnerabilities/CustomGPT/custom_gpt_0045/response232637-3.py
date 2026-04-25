
def run_module(name):
    carLists = ['what is your favorite car', 'car', 'sedan']
    if name in carLists:
        print('You like cars!')
        name3 = input('What is your favorite car? ')
        print(f'I also like {name3}!')
