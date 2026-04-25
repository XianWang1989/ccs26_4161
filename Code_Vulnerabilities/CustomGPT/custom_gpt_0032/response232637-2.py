
def check_food(name):
    food_lists = ['what is my food', 'pizza', 'burger', 'salad']  # Example list
    if name in food_lists:
        return f"You found the food: {name}"
    return None
