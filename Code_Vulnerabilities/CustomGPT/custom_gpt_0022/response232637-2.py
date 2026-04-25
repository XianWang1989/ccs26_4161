
def handle_question(question):
    carLists = ['what is my car', 'car']
    if question in carLists:
        return "This is about cars"
    return None
