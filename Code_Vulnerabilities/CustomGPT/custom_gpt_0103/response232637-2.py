
def play_vehicle_game():
    name = input('What vehicle do you prefer? ').lower()
    vehicle_list = ['car', 'bike', 'bus']

    if any(vehicle in name for vehicle in vehicle_list):
        print('You found a vehicle!')
