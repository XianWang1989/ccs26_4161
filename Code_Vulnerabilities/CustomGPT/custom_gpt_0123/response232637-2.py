
def run():
    name = input('Please enter your question about cars: ').lower()
    car_lists = ['what is my car', 'car']

    if name in car_lists:
        print('You found the car here')
