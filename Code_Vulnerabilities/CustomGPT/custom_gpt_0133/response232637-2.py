
def play_game():
    # Similar implementation for another topic, e.g., cars
    name = input('Please enter your question: ').lower()
    carLists = ['what is my favorite car', 'car', 'ford', 'toyota', 'bmw']

    if any(item in name for item in carLists):
        print('You found a car here!')
        # Add your logic for car-related responses
