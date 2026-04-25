
def handle_car_game(name):
    car_list = ['what is my car', 'car']
    if any(item in car_list for item in name):
        print('You found the car!')
        # Add more game logic here
