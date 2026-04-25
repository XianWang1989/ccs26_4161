
def check_foods(name):
    foodLists = ['what is my favorite food', 'food']
    for item in foodLists:
        if item in name:
            return True, "You found the food"
    return False, None
