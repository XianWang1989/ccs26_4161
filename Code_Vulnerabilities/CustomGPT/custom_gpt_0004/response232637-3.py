
def check_food(name):
    food_lists = ['what is my favorite food', 'food']
    if name in food_lists:
        print('You found a food topic!')
        return True
    return False
