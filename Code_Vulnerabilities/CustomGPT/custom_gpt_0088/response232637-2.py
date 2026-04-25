
def handle_question(question):
    food_lists = ['what is my favorite food', 'food']

    if question in food_lists:
        return "You've found the food!"
    return None
