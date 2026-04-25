
# MODULE1.py

def check_question(question):
    # For example, check if the question is related to colors
    color_keywords = ['color', 'what is my color']
    return any(keyword in question for keyword in color_keywords)

def run():
    # Logic specific to MODULE1
    name3 = input('What is your favorite color? ')
    if name3 == 'red':
        print('You are hot!')
    elif name3 == 'pink':
        print('You must be a lady')
    elif name3 == 'blue':
        print('Boys love this')
    else:
        print(f'Interesting choice of color: {name3}')
