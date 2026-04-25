
# MODULE1.py
def handle_question(question):
    color_list = ['what is my color', 'color']
    if question in color_list:
        print('You found the color here!')
        # Additional interactions
        return True  # Indicates that a module handled the question
    return False
