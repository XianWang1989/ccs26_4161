
def play_car_game(name):
    carLists = ['toyota', 'ford', 'bmw']
    for item in carLists:
        if item in name:
            print(f'You found the car: {item}')
