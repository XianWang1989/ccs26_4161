
def play_car_game():
    name = input('Ask your car-related question: ').lower()
    car_lists = ['what is my car', 'car']
    if any(item in name for item in car_lists):
        print('You found your car game!')
