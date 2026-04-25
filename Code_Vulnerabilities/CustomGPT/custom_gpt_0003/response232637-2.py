
# Similar structure but for cars
carLists = ['what is my car', 'car', 'sedan', 'SUV']

def check_cars(input_question):
    if any(car in input_question for car in carLists):
        print("You found a car!")
