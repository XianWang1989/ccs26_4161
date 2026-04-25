
# main.py
from package import MODULE1, MODULE2, MODULE3  # Import all relevant modules

name = input('Please Enter your question: ').lower()

if len(name) >= 3:
    MODULE1.play_color_game(name)
elif len(name) >= 3:  # Adjust as per your game condition
    MODULE2.play_car_game(name)
elif len(name) >= 3:
    MODULE3.play_food_game(name)
# You can continue for other modules as needed
else:
    print('Your question is too short!')
