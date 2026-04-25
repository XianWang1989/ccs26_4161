
def play_game(input_question):
    carLists = ['what is my car', 'car']
    if input_question in carLists:
        return f"You found the car here! What is your favorite car?"
    return None
