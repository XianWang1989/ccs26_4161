
# main.py
from package.MODULE1 import find_color
from package.MODULE2 import find_car

name = input('Please enter your question: ').lower()

# Check MODULE1 first
find_color(name)

# If MODULE1 does not handle the question/criteria, check MODULE2
if 'color' not in name:
    find_car(name)
