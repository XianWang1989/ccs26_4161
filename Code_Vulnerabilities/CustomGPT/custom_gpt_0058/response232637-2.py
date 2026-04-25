
def play_car_game():
    name = input('Please Enter your question about cars: ').lower()
    carLists = ['what is my car', 'car type']
    if name in carLists:
        print('You found the car-related question!')
