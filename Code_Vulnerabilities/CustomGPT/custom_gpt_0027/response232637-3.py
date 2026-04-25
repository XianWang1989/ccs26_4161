
def run_game(user_input):
    foodLists = ['pizza', 'burger', 'salad']  # Sample foods
    for item in user_input:
        if item in foodLists:
            print(f'You found the food: {item}')
