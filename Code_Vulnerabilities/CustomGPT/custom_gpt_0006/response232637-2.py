
def game_logic(name):
    car_lists = ['what is my car', 'car']
    if any(item in name for item in car_lists):
        print('You found the car here!')
        # Additional logic...
