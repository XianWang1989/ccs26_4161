
def play():
    question = input('Please Enter your question: ').lower()
    carLists = ['what is my favorite car', 'car']
    if question in carLists:
        print('You found the car here!')
