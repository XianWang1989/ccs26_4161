
def handle_query(query):
    car_lists = ['what is my favorite car', 'car']
    if query in car_lists:
        print('You found a car! What do you like?')
        return True
    return False
