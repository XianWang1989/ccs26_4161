
# MODULE2.py
def find_car(name):
    carLists = ['car', 'truck', 'bike']
    if any(car in name for car in carLists):
        print('You found a car-related question!')
        name3 = input('What type of car do you like? ')
        print(f'You like {name3}!')
