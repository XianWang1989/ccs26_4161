
def play_food_game():
    name = input('Ask your food-related question: ').lower()
    food_lists = ['what is my food', 'food']
    if any(item in name for item in food_lists):
        print('You found your food game!')
