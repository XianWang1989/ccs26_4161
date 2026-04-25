
def check_car_question(name):
    carLists = ['car', 'sports car', 'sedan']
    if any(item in name for item in carLists):
        return "You found a car here"
    return None
