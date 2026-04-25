
def process_question(question):
    car_list = ['car', 'truck', 'bike']  # Example list
    if any(car in question for car in car_list):
        print('You found a vehicle!')
        return True
    return False
