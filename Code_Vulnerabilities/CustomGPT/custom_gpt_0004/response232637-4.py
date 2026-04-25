
from package import MODULE1, MODULE2, MODULE3

name = input('Please enter your question: ').lower()

# Check each module's function
if not MODULE1.check_color(name):
    if not MODULE2.check_cars(name):
        MODULE3.check_food(name)
