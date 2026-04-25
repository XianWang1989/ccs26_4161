
# MODULE2.py
def handle_question(question):
    # Suppose this module deals with cars
    car_list = ['what is my favorite car', 'cars']
    if question in car_list:
        print('You found information about cars!')
        # Additional interactions
        return True  # Indicates that a module handled the question
    return False
