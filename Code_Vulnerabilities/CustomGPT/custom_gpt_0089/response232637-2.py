
def handle_input(name):
    vehicleLists = ['car', 'bike', 'bus']  # Sample list
    if any(vehicle in name for vehicle in vehicleLists):
        print('You found a vehicle!')
        # Further logic here...
