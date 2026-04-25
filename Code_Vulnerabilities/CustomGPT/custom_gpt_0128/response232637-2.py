
def handle_question(question):
    car_lists = ['what is my car', 'car']
    if question in car_lists:
        return "You found the car here!"
    return None
