
# MODULE2.py
def play_game(name):
    carLists = ['what is my car', 'car', 'sedan', 'truck']
    if any(item in carLists for item in name.split()):
        print('You found the car here!')
        # Additional game logic
