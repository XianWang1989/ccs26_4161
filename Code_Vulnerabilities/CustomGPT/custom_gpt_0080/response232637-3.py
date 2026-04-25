
# main.py
from package import MODULE1, MODULE2, MODULE3  # Import modules

name = input('Please enter your question: ').lower().split()  # Split input into words

if len(name) >= 3:
    MODULE1.check_color(name)
else:
    MODULE2.check_cars(name)
