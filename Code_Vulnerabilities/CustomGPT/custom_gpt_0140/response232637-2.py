
def check_cars(name2):
    carLists = ['what is my favorite car', 'car']
    for item in name2:
        if item in carLists:
            return True, 'car'
    return False, None
