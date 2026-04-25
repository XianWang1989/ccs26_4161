
from package import MODULE1, MODULE2, MODULE3, MODULE4

name = input('Please enter your question: ').lower().split()

if len(name) >= 3:
    MODULE1.play_color_game(name)
elif len(name) >= 2:
    MODULE2.play_car_game(name)
# Add further conditions for MODULE3 and MODULE4 as needed.
