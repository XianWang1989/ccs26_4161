
def handle_color_question(question):
    color_lists = ['what is my color', 'color', 'red', 'pink', 'blue']
    if question in color_lists:
        return "You found the color here!"
    else:
        return None
