
# MODULE1.py
def handle_question(question):
    color_lists = ['what is my color', 'color', 'red', 'pink', 'blue']
    if any(color in question for color in color_lists):
        return f'You found the color here! What is your favorite color?'
    return None
