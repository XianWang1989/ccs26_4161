
def check_car(name2):
    carLists = ['car', 'truck', 'bike']
    for item in name2:
        if item in carLists:
            print('You found a vehicle here')
            return True
    return False
