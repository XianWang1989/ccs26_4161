
# MODULE1.py
color_lists = ['what is my color', 'color', ...]

def handle_question(question):
    if question in color_lists:
        favorite_color = input('What is your favorite color? ')
        respond_to_color(favorite_color)
        return True
    return False

def respond_to_color(color):
    responses = {
        "red": "You are hot!",
        "pink": "You must be a lady.",
        "blue": "Boys love this."
    }
    print(responses.get(color, "I don't know that color."))
