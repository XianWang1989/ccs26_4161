
import re
import sys
from package import MODULE1, MODULE2, MODULE3  # Explicit imports

def get_color_response(name):
    if MODULE1.check_color(name):
        return MODULE1.get_color_response(name)
    elif MODULE2.check_car(name):
        return MODULE2.get_car_response(name)
    elif MODULE3.check_food(name):
        return MODULE3.get_food_response(name)
    else:
        return "No valid input found."

name = input('Please Enter your question: ').lower()
response = get_color_response(name)
print(response)
