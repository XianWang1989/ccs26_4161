
def handle_question(question):
    colorLists = ['what is my color', 'color']
    if question in colorLists:
        return "You found the color here"
    return None
