
def check_foods(name):
    foodLists = ['what is my favorite food', 'food']
    if any(item in name for item in foodLists):
        return 'food'
    return None
