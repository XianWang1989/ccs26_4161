
def run_module():
    name = input('Please enter your question: ').lower()
    car_list = ['car', 'truck', 'bike']
    if any(car in name for car in car_list):
        print('You found a car here!')
    return False  # Indicate if the question is not found
