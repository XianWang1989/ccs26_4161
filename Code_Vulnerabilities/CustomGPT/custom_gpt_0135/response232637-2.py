
def check_cars(input_text):
    car_list = ['car', 'truck', 'bike']
    for car in car_list:
        if car in input_text:
            return f"You found a vehicle: {car}"
    return None
