
# MODULE2.py
def run_car_game(name):
    car_lists = ['what is my favorite car?', 'car']
    if any(car in name for car in car_lists):
        print('You found a car!')
        # Implement car game logic here
    else:
        return False  # Indicate that the game didn't match
