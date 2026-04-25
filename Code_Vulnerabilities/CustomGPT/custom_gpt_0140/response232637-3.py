
def check_food(name2):
    foodLists = ['what is my favorite food', 'food']
    for item in name2:
        if item in foodLists:
            return True, 'food'
    return False, None
