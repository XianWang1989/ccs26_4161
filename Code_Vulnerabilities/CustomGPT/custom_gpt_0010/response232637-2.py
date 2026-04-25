
# MODULE2.py
def run_module():
    question = input('What is your question? ').lower()
    carLists = ['what is my car', 'car', 'toyota', 'ford']
    for item in question.split():
        if item in carLists:
            print('You found a car!')
            return True
    return False
