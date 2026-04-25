
def handle_input(name):
    car_list = ['sedan', 'SUV', 'convertible']
    if name in car_list:
        return f"You found a car type: {name}"
    return None
