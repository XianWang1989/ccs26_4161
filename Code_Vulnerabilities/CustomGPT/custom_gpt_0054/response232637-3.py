
carLists = ['car', 'truck', 'motorcycle']  # Example for cars

def check_answer(question):
    return any(car in question for car in carLists)

def respond():
    name3 = input('What is your favorite car? ')
    print(f'You chose: {name3}')
