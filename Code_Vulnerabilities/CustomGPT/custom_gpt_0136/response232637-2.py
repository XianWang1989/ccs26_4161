
# MODULE1.py
def process_question(question):
    if "color" in question:
        print('You found the color here.')
        name3 = input('What is your favorite color? ')
        if name3 == 'red':
            print('You are hot!')
        elif name3 == 'pink':
            print('You must be a lady.')
        elif name3 == 'blue':
            print('Boys love this.')
        return True  # Indicates the question was handled
    return False  # Indicates this module did not handle the question
