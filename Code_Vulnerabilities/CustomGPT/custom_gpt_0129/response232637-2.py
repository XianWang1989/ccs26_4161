
def handle_car_question(question):
    car_lists = ['what is my car', 'car', 'sedan', 'suv', 'truck']
    if question in car_lists:
        return "You found the car here!"
    else:
        return None
