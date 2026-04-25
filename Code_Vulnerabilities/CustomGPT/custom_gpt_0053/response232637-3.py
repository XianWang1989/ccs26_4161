
from package import MODULE1, MODULE2, MODULE3  # Import your modules

name = input('Please enter your question: ').lower()
name2 = name.split()  # Split input for checking in lists

# Check through modules
MODULE1.handle_color_game(name2)
MODULE2.handle_car_game(name2)
MODULE3.handle_food_game(name2)  # Assuming you have similar logic in MODULE3
# Add calls for MODULE4 and others as needed
