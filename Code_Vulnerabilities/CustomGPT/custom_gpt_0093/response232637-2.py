
# MODULE2.py
def handle_question(question):
    # Example for cars
    car_lists = ['what is my car', 'cars', 'toyota', 'ford']
    if any(car in question for car in car_lists):
        return 'You are asking about cars!'
    return None
