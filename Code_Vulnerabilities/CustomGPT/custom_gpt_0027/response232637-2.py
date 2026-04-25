
def run_game(user_input):
    carLists = ['toyota', 'honda', 'ford']  # Sample cars
    for item in user_input:
        if item in carLists:
            print(f'You found the car: {item}')
