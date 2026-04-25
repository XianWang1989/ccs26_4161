
def check_food(name2):
    foodLists = ['apple', 'banana', 'cake']
    for item in name2:
        if item in foodLists:
            print('You found a food here')
            return True
    return False
