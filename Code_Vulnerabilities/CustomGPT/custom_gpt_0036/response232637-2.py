
# MODULE2.py
def play_car_game():
    print("Welcome to the car game!")
    question = input('Please enter your question about cars: ').lower()
    carBrands = ['ford', 'toyota', 'bmw']

    for brand in carBrands:
        if brand in question:
            print(f'You mentioned: {brand}')
            return True  # Game played
    return False  # Game not played
