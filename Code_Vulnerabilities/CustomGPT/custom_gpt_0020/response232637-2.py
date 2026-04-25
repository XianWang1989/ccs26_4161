
def process_car_game(name):
    carLists = ['car', 'truck', 'motorcycle']  # Example car list
    for item in name:
        if item in carLists:
            print('You mentioned a vehicle!')
