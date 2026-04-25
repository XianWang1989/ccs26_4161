
def play_car_game(name):
    carLists = ['what is my favorite car', 'car', ...] # your list for cars
    if any(item in name for item in carLists):
        print('You found a car here')
        # Handle car-related questions or games...
