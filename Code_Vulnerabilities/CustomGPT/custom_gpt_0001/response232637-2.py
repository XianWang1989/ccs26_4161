
def run_module():
    car_lists = ['car', 'sedan', 'suv']  # example list; should contain relevant checks.
    name = input('Please Enter your question: ').lower()
    if any(car in name for car in car_lists):
        print('You found a car related query!')
