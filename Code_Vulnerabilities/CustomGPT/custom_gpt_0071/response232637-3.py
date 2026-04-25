
# MODULE2.py
car_lists = ['what is my car', 'cars', ...]

def handle_question(question):
    if question in car_lists:
        # Handle questions about cars
        print("This is about cars!")
        return True
    return False
