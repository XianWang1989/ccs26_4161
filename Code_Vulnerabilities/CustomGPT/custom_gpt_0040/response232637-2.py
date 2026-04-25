
def play_game(name):
    carLists = ['car', 'truck', 'bike']  # Example car list
    if any(car in name for car in carLists):
        print('Let\'s talk about cars!')
