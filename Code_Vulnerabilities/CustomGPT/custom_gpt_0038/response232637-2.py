
def handle_car_question(name):
    car_lists = ['what is my car', 'car', 'sedan', 'SUV']
    for item in car_lists:
        if item in name:
            print('You found a car related question!')
            # Additional logic for car questions
