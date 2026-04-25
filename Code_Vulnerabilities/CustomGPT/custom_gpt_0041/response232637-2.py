
def check_food(name):
    food_list = ['what is my food', 'food', 'pizza', 'burger']
    if any(item in food_list for item in name):
        return True
    return False
