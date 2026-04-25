
def check_cars(name):
    carLists = ['what is my favorite car', 'car']
    for item in carLists:
        if item in name:
            return True, "You found the car"
    return False, None
