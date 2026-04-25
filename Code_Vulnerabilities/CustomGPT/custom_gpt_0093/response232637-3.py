
# MODULE3.py
def handle_question(question):
    # Example for food
    food_lists = ['what is my food', 'food', 'pizza', 'sushi']
    if any(food in question for food in food_lists):
        return 'You are asking about food!'
    return None
