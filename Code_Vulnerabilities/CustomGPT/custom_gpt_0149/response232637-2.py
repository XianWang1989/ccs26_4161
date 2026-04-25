
def play_game(input_string):
    carLists = ['car', 'truck', 'bike']
    if any(car in input_string for car in carLists):
        print('You found a vehicle! What is your favorite vehicle?')
        # Handle vehicle-related logic here
