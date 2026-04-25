
from package import MODULE1, MODULE2

name = input('Please enter your question: ').lower()

# Check MODULE1
MODULE1.check_color(name)

# Check MODULE2 if MODULE1 didn't handle the question
if len(name) < 3 or name not in ['what is my color', 'color', 'red', 'pink', 'blue']:
    MODULE2.check_cars(name)
