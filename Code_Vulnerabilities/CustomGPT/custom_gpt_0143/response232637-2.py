
def play_game(name):
    car_lists = ['what car do you like', 'car', 'favorite car']
    if name in car_lists:
        response = input('What is your favorite car? ')
        print(f'Nice choice with the {response}!')
