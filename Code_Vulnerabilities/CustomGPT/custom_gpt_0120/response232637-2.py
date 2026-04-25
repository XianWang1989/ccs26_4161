
# MODULE2.py
def game_logic(name):
    # Similar game logic for cars, etc.
    car_list = ['car', 'truck', 'bike']
    for item in car_list:
        if item in name:
            print(f'You found the car: {item}')
            return True
    return False
