
# package/MODULE1.py
color_lists = ['what is my color', 'color', 'red', 'pink', 'blue']

def check_question(question):
    return question in color_lists

def answer_question():
    name3 = input("What is your favorite color? ")
    if name3 == 'red':
        return 'You are hot!'
    elif name3 == 'pink':
        return 'You must be a lady.'
    elif name3 == 'blue':
        return 'Boys love this.'
    else:
        return 'Color not recognized.'
