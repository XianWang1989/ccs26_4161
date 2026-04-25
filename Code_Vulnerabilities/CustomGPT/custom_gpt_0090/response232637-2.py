
def check_cars(name):
    carLists = ['what is my favorite car', 'car']
    if any(item in name for item in carLists):
        return 'car'
    return None
