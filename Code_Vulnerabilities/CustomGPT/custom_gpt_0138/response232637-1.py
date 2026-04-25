
def check_color_question(name):
    colorLists = ['what is my color', 'color']  # Add more colors as needed
    if name in colorLists:
        return True
    return False

def respond_to_color(name3):
    responses = {
        'red': 'You are hot!',
        'pink': 'You must be a lady',
        'blue': 'Boys love this'
    }
    return responses.get(name3, "I don't know that color.")
