
def check_car_question(name):
    carLists = ['what is my car', 'car']  # Add more car questions
    if name in carLists:
        return True
    return False

def respond_to_car(name3):
    responses = {
        'ferrari': 'Fast and furious!',
        'toyota': 'Reliable choice!'
    }
    return responses.get(name3, "I don't know that car.")
