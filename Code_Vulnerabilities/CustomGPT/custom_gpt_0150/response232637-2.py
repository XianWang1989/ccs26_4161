
# MODULE1.py
def process_question(question):
    colorLists = ['what is my color', 'color', ...]  # Sample list of items
    if any(item in question for item in colorLists):
        print('You found the color here!')
        name3 = input('What is your favorite color? ')
        respond_to_color(name3)
        return True
    return False

def respond_to_color(color):
    if color == 'red':
        print('You are hot!')
    elif color == 'pink':
        print('You must be a lady')
    elif color == 'blue':
        print('Boys love this')
    # Add more colors as needed
