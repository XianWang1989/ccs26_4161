
def play():
    question = input('Please Enter your question: ').lower()
    foodLists = ['what is my favorite food', 'food']
    if question in foodLists:
        print('You found the food here!')
