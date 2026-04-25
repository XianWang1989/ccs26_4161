
def check_foods(name):
    food_lists = ['what is my favorite food', 'food']
    if any(item in food_lists for item in name):
        print('You found food here')
        # Additional logic for foods...
