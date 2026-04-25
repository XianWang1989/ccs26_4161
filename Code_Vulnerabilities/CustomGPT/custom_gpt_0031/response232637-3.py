
def run_module():
    name = input('Please enter your question: ').lower()
    food_list = ['pizza', 'burger', 'pasta']
    if any(food in name for food in food_list):
        print('You found food here!')
    return False  # Indicate if the question is not found
