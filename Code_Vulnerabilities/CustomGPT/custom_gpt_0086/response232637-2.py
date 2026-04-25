
# MODULE2.py
def play_car_game():
    name = input('Please enter your car question: ').lower()
    car_lists = ['what is my car', ...]  # Add your car questions here
    if any(item in name for item in car_lists):
        print('You found a car-related question!')
