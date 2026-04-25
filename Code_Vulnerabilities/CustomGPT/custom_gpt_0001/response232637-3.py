
def run_module():
    food_lists = ['pizza', 'burger', 'salad']  # example list; should contain relevant checks.
    name = input('Please Enter your question: ').lower()
    if any(food in name for food in food_lists):
        print('You found a food related query!')
