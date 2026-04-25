
def check_cars(name):
    car_lists = ['ford', 'toyota', 'honda']
    for item in name:
        if item in car_lists:
            print(f'Found a car: {item}')
            return True
    return False
