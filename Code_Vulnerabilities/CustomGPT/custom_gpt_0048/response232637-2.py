
def play_game(name2):
    carLists = ['what is my favorite car', 'car']
    for item in name2:
        if item in carLists:
            print('You found the car here!')
            name3 = input('What is your favorite car? ')
            print(f'Nice choice: {name3}')
