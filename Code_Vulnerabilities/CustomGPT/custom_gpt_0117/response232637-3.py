
def play_car_game(user_input):
    carLists = ['car', 'truck', 'bike']
    if any(car in user_input for car in carLists):
        return "Let's talk about cars!"
    return None
