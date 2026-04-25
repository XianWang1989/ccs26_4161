
def play_game(input_question):
    colorLists = ['what is my color', 'color']
    if input_question in colorLists:
        return f"You found the color here! What is your favorite color?"
    return None
