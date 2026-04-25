
def handle_question(question):
    color_lists = ['what is my color', 'color']

    if question in color_lists:
        return "You found the color here"
    return None
