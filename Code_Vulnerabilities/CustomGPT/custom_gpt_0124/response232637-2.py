
def check_cars(name):
    car_lists = ['what is my favorite car', 'car']
    if any(item in car_lists for item in name):
        print('You found a car here')
        # Additional logic for cars...
